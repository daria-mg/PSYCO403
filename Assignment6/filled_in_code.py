from psychopy import gui, core, visual, monitors, event
import numpy as np
import random 
import os 
from datetime import datetime 

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr': '',
            'age': '',
            'gender': '',
            'handedness': ('right', 'left', 'ambi'),
            }
print(exp_info)
print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                    title ="subject info",
                    fixed = ['session'],
                    order =['session', 'subject_nr', 'gender', 'handedness'])

#get date and time
date = datetime.now()
exp_info['date']=str(date.day) + '/' + str(date.month) + '/' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
file_name = str(part_info['subject_nr']) + '-' + exp_info['date'] + '.csv'
print(file_name)

#define where to store the data
main_dir = os.getcwd()
sub_dir = os.path.join(main_dir, 'sub_info', file_name)

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=32.4, distance=60)
mon.setSizePix([1024,768])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
window=visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1], units='pix', fullscr=True)

#-define experiment start text using psychopy functions
mytext = visual.TestStim(win, text=start_msg)

#-define block (start)/end text using psychopy functions
mytext.draw()
win.flip()
event.waitKeys()
win.close()

#-define stimuli using psychopy functions
mytext = visual.TextStim(win)
mytext.text = start_msg
mytext.text = block_msg
mytext.text = endtrial_msg

#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_txt = visual.TextStim(win, text=start_msg)
start_txt.draw()
win.flip()

#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(nBlocks):
    #-present block start message
    block_txt=visual.TextStim(win, text=block_msg)
    block_txt.draw()
    win.flip()
    event.waitKeys()
    
    #-randomize order of trials here 
    np.random.shuffle(zippedlist)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================
    #-for loop for nTrials *
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image.image=os.path.joint(image_dir, stim[trial]
        #-empty keypresses
        
        #====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        fixation_text.draw()
        #-flip window
        win.flip()
        event.waitKeys()
        
        #-wait time (stimulus duration)
        core.wait(2.0)
        
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()