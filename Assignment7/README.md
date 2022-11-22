## WAIT EXERCISES

###### Q1.

#===================== START TRIAL =====================#

#-draw fixation

        fix_text.draw()

#-flip window

        win.flip()

#-wait time (stimulus duration)

        core.wait(1.0)

#-draw image

        my_image.draw()

#-flip window

        win.flip()

#-wait time (stimulus duration)

        core.wait(1.0)

#-draw end trial text

        end_trial_text.draw()

#-flip window

        win.flip()

#-wait time (stimulus duration)

        core.wait(1.0)



## CLOCK EXERCISES
###### Q1.

        from psychopy import visual, monitors, event, core
        import os
        import numpy as np

        mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
        mon.setSizePix([1024,768])
        win = visual.Window(monitor=mon)

        main_dir=os.getcwd()
        image_dir=os.path.join(main_dir, 'images_jpg')

        my_image = visual.ImageStim(win, units="pix",size=(400,400))
        stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
        nTrials = 3
        wait_timer = core.Clock()

        end_trial_msg = "End of trial"
        end_trial_txt = visual.TextStim(win, text = end_trial_msg)
        fix_txt = visual.TextStim(win, text = "+")

        for trial in range(nTrials):
            my_image.image = os.path.join(image_dir, stimulus[trial])
            fix_txt.draw()
            win.flip()
            core.wait(1.0)

            my_image.draw()
            win.flip()
            img_StartTime = wait_timer.getTime()
            core.wait(2.0)
            img_EndTime = wait_timer.getTime()

            fix_txt.draw()
            win.flip()
            core.wait(1.0)

            print("Image duration was {} seconds".format(img_EndTime - img_StartTime))

        win.close()

Results when above code is executed:

-Image duration was 2.001221466984134 seconds

-Image duration was 2.0013763409806415 seconds

-Image duration was 2.0001357899745926 seconds

All of the image durations were around 2.0 seconds, however, the durations were all slightly above 2.0 seconds when looking at the how number. I would say that core.wait() is pretty precise considering that all the image durations are very close to 2.0 seconds.


###### Q2.
        from psychopy import visual, monitors, event, core
        import os

        mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
        mon.setSizePix([1024,768])
        win = visual.Window(monitor=mon)

        main_dir=os.getcwd()
        image_dir=os.path.join(main_dir, 'images_jpg')

        my_image = visual.ImageStim(win, units="pix",size=(400,400))
        stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
        nTrials = 3

        wait_timer = core.Clock()
        StimTimer = core.Clock()

        end_trial_msg = "End of trial"
        end_trial_txt = visual.TextStim(win, text = end_trial_msg)
        fix_txt = visual.TextStim(win, text = "+")

        for trial in range(nTrials):
            my_image.image = os.path.join(image_dir, stimulus[trial])
            StimTimer.reset()

            while StimTimer.getTime() <= 1.0:
                fix_txt.draw()
                win.flip()

            img_StartTime = wait_timer.getTime()
            while 1 < StimTimer.getTime() <=2:
                my_image.draw()
                win.flip()
            img_EndTime = wait_timer.getTime()

            fix_txt.draw()
            win.flip()

            print("Image duration was {} seconds".format(img_EndTime - img_StartTime))

        win.close()

Results when above code is executed:

-Image duration was 0.9992309350054711 seconds

-Image duration was 1.0000521530164406 seconds

-Image duration was 0.9995522829703987 seconds

This method used in Q2 is less precise than the method used in Q1 (core.wait). When this code is executed, two of the values are below 1 second and one value is slightly above 1 second. While the values are close to 1 second, I would say that the first method is more precise.

###### Q3.
        from psychopy import visual, monitors, event, core
        import os

        mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
        mon.setSizePix([1024,768])
        win = visual.Window(monitor=mon)

        main_dir=os.getcwd()
        image_dir=os.path.join(main_dir, 'images_jpg')

        my_image = visual.ImageStim(win, units="pix",size=(400,400))
        stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
        nTrials = 3

        wait_timer = core.Clock()
        StimTimer = core.CountdownTimer()

        end_trial_msg = "End of trial"
        end_trial_txt = visual.TextStim(win, text = end_trial_msg)
        fix_txt = visual.TextStim(win, text = "+")

        for trial in range(nTrials):
            my_image.image = os.path.join(image_dir, stimulus[trial])

            fix_txt.draw()
            win.flip()
            core.wait(1.0)

            StimTimer.reset()
            StimTimer.add(1)
            img_StartTime = wait_timer.getTime()

            while StimTimer.getTime() > 0:
                my_image.draw()
                win.flip()
            img_EndTime = wait_timer.getTime()

            fix_txt.draw()
            win.flip()
            core.wait(1.0)

            print("Image duration was {} seconds".format(img_EndTime - img_StartTime))

        win.close()

Results when above code is executed:

-Image duration was 1.0027119260048494 seconds

-Image duration was 1.002293716010172 seconds

-Image duration was 1.0032791859703138 seconds

I believe that this method is slightly less precise than the first method and slightly more precise than the second method. All of the values were around the same value, however, they all were slightly above one second. 

###### Q4.
#===================== BLOCK SEQUENCE =====================#

        block_timer = core.Clock()
        trial_timer = core.Clock()
        wait_timer = core.Clock()

        #-for loop for nBlocks *
        for block in range(nBlocks):
            block_txt=visual.TextStim(win, text=block_msg)
            block_txt.draw()
            win.flip()
            event.waitKeys()

            #-randomize order of trials here 
            np.random.shuffle(zippedlist)

            #-reset response time clock here
            block_timer.reset()
            block_timer.add(1.0)
            block_StartTime = wait_timer.getTime()

            #=====================
            #TRIAL SEQUENCE
            #=====================
            #-for loop for nTrials *
            for trial in range(nTrials):
                #-set stimuli and stimulus properties for the current trial
                my_image.image=os.path.joint(image_dir, stimulus[trial]
                my_image = visual.ImageStim(win, unit = "pix", size = (400,400))

                #====================
                #START TRIAL
                #=====================   
                fix_txt.draw()
                win.flip()
                core.wait(2.0)

                trial_timer.reset()
                trial_timer.add(1.0)
                img_StartTime = wait_timer.getTime()

                while trial_timer.getTime() > 0:
                    my_image.draw()
                    win.flip()
                img_EndTime = wait_timer.getTime()

                end_trial_txt.draw()
                win.flip()
                core.wait(1.0)

                print("Image duration was {} seconds".format(img_EndTime - img_StartTime))

#====================== END OF EXPERIMENT======================#     
        #-close window
        
                win.close()

## FRAME-BASED TIMING EXERCISES 
###### Q1.
        from psychopy import visual, monitors, core, event 
        import os 

        mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
        mon.setSizePix([1024,768])
        win = visual.Window(monitor=mon)

        main_dir=os.getcwd()
        image_dir=os.path.join(main_dir, 'images_jpg')

        #frame timing
        refresh = 1.0/6.0
        fix_duration = 0.2
        image_duration = 0.1
        text_duration = 0.2

        fix_frames = int(fix_duration/refres)
        image_frames = int(image_duration/refresh)
        text_frames = int(text_duration/refresh)
        total_frames = int(fix_frames + image_frames + text_frames)

        stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
        my_image = visual.ImageStim(win, units="pix",size=(400,400))

        #nTrials = 3
        #nBlocks = 2

        #trial_timer = core.Clock()
        #block_timer = core.Clock()

        for frame_num in range(total_frames):
            if 0 <= frame_num <= fix_frames:
                fix_txt.draw()
                win.flip()
                core.wait(1.0)

                if frame_num == fix_frames:
                    print("End fix frame =", frame_num)

            if fix_frames < frame_num <= (fix_frames + image_frames):
                my_image.draw()
                win.flip()

                if frame_num == (fix_frames + image_frames):
                    `print("End image frame =", frame_num)

            if (fix_frames + image_frames) < frame_num < total_frames:
                end_trial_txt.draw()
                win.flip()
                core.wait(1.0)

                if frame_num == (total_frames-1):
                    print("End text frame =", frame_num)

        win.close()

###### Q2.
        from psychopy import visual, monitors, core, event, logging
        import os 

        mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
        mon.setSizePix([1024,768])
        win = visual.Window(monitor=mon)

        main_dir=os.getcwd()
        image_dir=os.path.join(main_dir, 'images_jpg')

        #frame timing
        refresh = 1.0/6.0
        fix_duration = 0.2
        image_duration = 0.1
        text_duration = 0.2

        fix_frames = int(fix_duration/refres)
        image_frames = int(image_duration/refresh)
        text_frames = int(text_duration/refresh)
        total_frames = int(fix_frames + image_frames + text_frames)

        win.recordFrameIntervals = True 
        win.refreshThreshold = 1.0/6.0 + 0.004
        logging.console.setLevel(logging.WARNING)

        stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
        my_image = visual.ImageStim(win, units="pix",size=(400,400))

        #nTrials = 3
        #nBlocks = 2

        #trial_timer = core.Clock()
        #block_timer = core.Clock()

        #start trial 
        for frame_num in range(total_frames):
            if 0 <= frame_num <= fix_frames:
                fix_txt.draw()
                win.flip()
                core.wait(1.0)

                if frame_num == fix_frames:
                    print("End fix frame =", frame_num)

            if fix_frames < frame_num <= (fix_frames + image_frames):
                my_image.draw()
                win.flip()

                if frame_num == (fix_frames + image_frames):
                    `print("End image frame =", frame_num)

            if (fix_frames + image_frames) < frame_num < total_frames:
                end_trial_txt.draw()
                win.flip()
                core.wait(1.0)

                if frame_num == (total_frames-1):
                    print("End text frame =", frame_num)

                print("Overall, %i frames were dropped." %win.nDroppedFrames)

        win.close()

