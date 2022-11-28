# Psychopy Keypress Exercises
###### Q1
    from psychopy import event, visual, monitors, core

    mon = monitors.Monitor('myMonitor',width=32.4, distance=60)
    mon.setSizePix([1024,768])
    win = visual.Window(monitor=mon, size=(400,400), color=(-1,-1,-1))

    my_text = visual.TextStim(win)
    nTrials = 10 

    rt_clock = core.Clock() #response time clock
    cd_timer = core.CountdownTimer() #countdown timer

    event.clearEvents(eventType='keyboard') 

    for trial in range(nTrials):
        rt_clock.reset()
        cd_timer.add(2)
        #event.clearEvents(eventType='keyboard') -- (for question #2)
        count=-1
        while cd_timer.getTime()>0:
            my_text.text = "please make a keypress for trial %i" % trial 
            my_text.draw()
            win.flip()
            keys = event.getKeys(keyList=['1', '2', 'escape'])
            if keys:
                count=count+1
                if count == 0:
                    resp_time = rt_clock.getTime()
                    sub_resp = keys
                    print(sub_resp, resp_time)
                if 'escape' in keys:
                    win.close()
    win.close()


###### Q2

When event.ClearEvents was placed inside vs. outside the trial loop, the results were the same. The trial loop worked, only the first keypress was recorded, and when no keypress was performed no response was recorded. Changing the location of this piece of code did not affect what was printed in the output window. When I unindent the "if keys:" line, the trial loop breaks and no responses are collected/recorded in the output window. Each trial is up on the screen for two seconds, however, no response is collected and the next trial starts. Because the "if key:" line is not indented properly, there is an indentation error which will affect how the code is ran.



