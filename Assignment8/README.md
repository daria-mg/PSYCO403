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



# Recording Data Exercises 
###### Q1

        from psychopy import event, visual, monitors, core
        import numpy as np

        mon = monitors.Monitor('myMonitor',width=32.4, distance=60)
        mon.setSizePix([1024,768])
        win = visual.Window(monitor=mon, size=(400,400), color=(-1,-1,-1))

        nTrials = 4
        nBlocks = 2
        my_text = visual.TextStim(win)
        rt_clock=core.Clock()
        cd_timer=core.CountdownTimer()

        #Q2 dictionaries:
        sub_resp = dict()
        sub_acc = dict()
        prob = dict()
        corr_resp = dict()
        resp_time = dict()

        math_problems = ['1+3=', '1+1=', '3-2=', '4-1=']
        solutions = [4,2,1,3]
        prob_sol=list(zip(math_problems, solutions))

        sub_resp = [[0]*nTrials]*nBlocks
        sub_acc = [[0]*nTrials]*nBlocks
        prob = [[0]*nTrials]*nBlocks
        corr_resp = [[0]*nTrials]*nBlocks
        resp_time = [[0]*nTrials]*nBlocks

        for block in range(nBlocks):
            sub_resp[block] = [-1]*nTrials
            sub_acc[block] = [-1]*nTrials
            prob[block] = [-1]*nTrials
            corr_resp[block] = [-1]*nTrials
            resp_time[block] = [-1]*nTrials
            for trial in range(nTrials):
                prob[block][trial] = prob_sol[np.random.choice(4)]
                corr_resp[block][trial] = prob[block][trial][1]
                rt_clock.reset()
                cd_timer.add(3)
                event.clearEvents(eventType='keyboard')
                count=-1
                while cd_timer.getTime()>0:
                    my_text.text = prob[block][trial][0]
                    my_text.draw()
                    win.flip()
                    keys=event.getKeys(keyList=['1','2','3','4','escape'])
                    if keys:
                        count=count+1
                        if count == 0:
                            resp_time[block][trial]=rt_clock.getTime()
                            sub_resp[block][trial]=keys[0]

                if sub_resp[block][trial] == str(corr_resp[block][trial]):
                    sub_acc[block][trial] = 1
                elif sub_resp[block][trial] != str(corr_resp[block][trial]):
                    sub_acc[block][trial] = 2

                print('problem=', prob[block][trial], 'correct response=', corr_resp[block][trial], 'subject response=', sub_resp[block][trial], 'subject accuracy=', sub_acc[block][trial], 'response time=', resp_time[block][trial])

        win.close()

        print(prob)
        print(corr_resp)
        print(sub_resp)
        print(sub_acc)


