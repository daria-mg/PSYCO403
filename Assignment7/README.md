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

trial_timer = core.Clock()

main_dir=os.getcwd()
image_dir=os.path.join(main_dir, 'experiments', 'stimulus')

stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
my_image = visual.ImageStim(win, units="pix",size=(400,400))

nTrials = 3

for trial in range(nTrials):
    trial_timer.reset()
    core.wait(1.0)
    print('Trial' + str(trial) + ' time: ', trial_timer.getTime())
    my_image.image = os.path.join(image_dir, stimulus[trial])
    my_image.draw()
    win.flip()

win.close()

###### Q2.
from psychopy import visual, gui, monitors, event, core
import os
import numpy as np
from PIL import Image

mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
mon.setSizePix([1024,768])
win = visual.Window(monitor=mon)
main_dir=os.getcwd()
image_dir=os.path.join(main_dir, 'Images')

trial_time = core.Clock()

stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
my_image = visual.ImageStim(win, units="pix",size=(400,400))
nTrials = 3

for trial in range(nTrials):
    trial_timer.reset()
    my_image.draw()
    while trial_timer.getTime()<=1.0:
        print('Trial' + str(trial) + ' time: ', trial_timer.getTime())
    my_image.image = os.path.join(image_dir, stimulus[trial])
    my_image.draw()
    win.flip()

win.close()

###### Q3.
from psychopy import visual, monitors, event, core
import os
import numpy as np
from PIL import Image

mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
mon.setSizePix([1024,768])
win = visual.Window(monitor=mon)

trial_time = core.Clock()
pres_timer=core.CountdownTimer()

os.chdir('/Desktop')
main_dir=os.getcwd()
image_dir=os.path.join(main_dir, 'Images')

stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']
my_image = visual.ImageStim(win, units="pix",size=(400,400))

nTrials = 3

for trial in range(nTrials):
    pres_timer.reset()
    pres_timer.add(1.0)
    my_image.draw()
    while pres_timer.getTimer() > 0:
        print('Trial' + str(trial) + ' time: ', pres_timer.getTime())
    my_image.image = os.path.join(image_dir, stimulus[trial])
    my_image.draw()
    win.flip()

win.close()

###### Q4.
from psychopy import visual, monitors, event, core
import os
import numpy as np
from PIL import Image

mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
mon.setSizePix([1024,768])
win = visual.Window(monitor=mon)

fix_text = visual.TextStim(win, text="+")
my_image = visual.ImageStim(win)
end_trial_txt = visual.TextStim(win, text=end_trial_msg)

stimulus = ['face01.jpg', 'face02.jpg', 'face03.jpg']

nTrials = 3
nBlocks = 2

wait_timer = core.Clock()
clock_wait_timer = core.Clock()
countdown_timer = core.CountdownTimer()

#===================== START TRIAL =====================# 

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stimulus[trial])
    fix_text.draw()
    win.flip()
    core.wait(1.0)
    countdown_timer.reset())
    countdown_timer.addTime(1)
    img_StartTime = wait_timer.getTime()
    while countdown_timer.getTimer() > 0:
        my_iimage.draw()
        win.flip()
        
    img_EndTime = wait_timer.getTime()
    
    print("image duration was {} seconds".format(img_EndTime - img_StartTime))
    
    end_trial_txt.draw()
    win.flip()
    core.wait(1.0)

win.close()

## FRAME-BASED TIMING EXERCISES 
###### Q1.
from psychopy import visual, monitors, core, event, logging 
import os 
import numpy as np

mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
mon.setSizePix([1024,768])
win = visual.Window(monitor=mon)

os.chdir('/Desktop')
main_dir=os.getcwd()
image_dir=os.path.join(main_dir, 'Images')

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

nTrials = 3
nBlocks = 2

trial_timer = core.Clock()
block_timer = core.Clock()

for frame_num in range(total_frames):
    if 0 <= frame_num <= fix_frames:
        win.flip()
        
        if frame_num == fix_frames:
            print("End fix frame =", frame_num)
    
    if fix_frames < frame_num <= (fix_frames + image_frames):
        win.flip()
        
        if frame_num == (fix_frames + image_frames):
            `print("End image frame =", frame_num)
    
    if (fix_frames + image_frames) < frame_num < total_frames:
        win.flip()
        
        if frame_num == (total_frames-1):
            print("End text frame =", frame_num)

win.close()

###### Q2.


