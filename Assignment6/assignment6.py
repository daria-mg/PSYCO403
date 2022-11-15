from psychopy import gui, core, visual, monitors, event
import numpy as np
import random 
import os 
from datetime import datetime 

#DIALOG BOX EXERCISES
#Q1.
exp_info = {'subject_nr':0,
            'age':0,
            'handedness':('right','left', 'ambi'),
            'gender':('male','female','other','prefer not to say'),
            'session':1
            }

#Q2.
exp_info = {'subject_nr':0,
            'age':0,
            'handedness':('right','left', 'ambi'),
            'gender':(),
            'session':1
            }

#Using DlgFromDicr:
#Q1.
my_dlg=gui.DlgFromDict(dictionary=exp_info, title="subject info")

#Q2.
my_dlg=gui.DlgFromDict(dictionary=exp_info, title="subject info", fixed=['session 1'])
#When the variable "session" is set as fixed, the participant cannot change the value and 
#the session stays as "1".

#Q3.
exp_info = {'session':1,
            'subject_nr': '',
            'age': '',
            'gender': '',
            'handedness': ('right', 'left', 'ambi'),
            }

my_dlg=gui.DlgFromDict(dictionary=exp_info, 
                        title="subject info",
                        fixed=['session'],
                        show=False
                        )
#Q4.
print("All variables have been created! Now ready to show the dialog box!")

my_dlg=gui.DlgFromDict(dictionary=exp_info, 
                        title ="subject info",
                        fixed = ['session'],
                        order =['session', 'subject_nr', 'gender', 'handedness'],
                        show = True
                        )

#Q5.
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


#MONITOR AND WINDOW EXERCISES
#Q1: How does changing "units" affect how you define window size?
    #The unit values can be "none', 'height', 'norm', 'deg','cm','pix'. Depending on the circumstance, you can change 
    #the units so that the images are displayed clearly. Changing 'norm' and 'height' allows the images to scale naturally 
    #with the window size on the device you are using. For example, a phone screen vs. a computer screen will need different 
    #units so that the stimulus is displayed properly. 'cm' measures the centimeters of the screen and 'deg' measures the degreee 
    #of visual angle. Changing any of these units will affect how the stimulus is displayed on the screen and depending on the device 
    #used, the units should be changed so that the stimulus can be displayed properly/clearly. 

#Q2: How does changing colorSpace affect how you define the color of your window? Can you define colors by name?
    #By changing the colorSpace, the way the color is defined is also changed. PsycoPy has three basic colorSpaces that it uses: RGB, 
    #DKL, and LMS. The range for RGB and LMS include values only between -1 to 1 that are used to create a triplet of values [0,0,0].
    #DKL also uses a triplet code - [0,0,0] - but the values included in the range are a lot more. Colors can be specified by a name 
    #(ie. "aliceblue") and even by a hexadecimal string. The web/X11 color names can be used to specify a color and these names are 
    #then converted in RGB colorSpace in Psychopy. 

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=30.4, distance=60)
mon.setSizePix([2880,1880])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win=visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1], units='pix', fullscr=True)


#STIMULUS EXERCISES
#Q1.
main_dir=os.getcwd()
print(main_dir)
image_dir=os.path.join(main_dir, 'images')

stimulus = ['face01.jpg', 'face02.jpg','face03.jpg','face04.jpg', 'face05.jpg','face06.jpg','face07.jpg', 'face08.jpg','face09.jpg', 'face10.jpg']

nTrials=10
my_image=visual.ImageStim(win, units="pix", size=(400,400))
np.random.shuffle(stimulus)

for trial in range(nTrials):
    my_image.image=os.path.join(image_dir, stimulus[trial])
    my_image.draw()
    win.flip()
    event.waitKeys()
win.close()

#Q2.
mon=monitors.Monitor('myMonitor', width=30.4, distance=60)
mon.setSizePix([2880,1880])
mon.save()

sSize = mon.getSizePix()
sWidth = iSize[0]
sHeight = iSize[1]
win = visual.Window(monitor=mon, fullscr=True)

text =visual.TextStim(win, text = '+')
image=visual.ImageStim(win, units='pix', size = (400,400))
image_dir = os.path.join(main_dir, 'images')
stimulus = ['face01.jpg', 'face02.jpg','face03.jpg','face04.jpg', 'face05.jpg','face06.jpg','face07.jpg', 'face08.jpg','face09.jpg', 'face10.jpg']
nTrials = 10

horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1]
vertiMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1]

for trial in range(nTrials):
    image.image = os.path.join(image_dir, stimulus[trial])
    image.position = (horizMult[trial] * sWidth/4, verMult[trial] * sHeight/4)
    image.draw()
    fixation.draw()
    win.flip()
    event.waitKeys()

win.close()

#Q3.
fixation=visual.TextStim(win, text='+')

#Q4.
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text using psychopy functions
start_msg = "Welcome to the experiment. Please press any key to continue."
start_txt = visual.TextStim(win, text=start_msg)

#-define block (start)/end text using psychopy functions
block_smsg = "Press any key to proceed to the next block"
block_emsg = "End of block"
block_stxt = visual.TextStim(win, text=block_smsg)
block_emsg = visual.TextStim(win, text=block_emsg)

#-define stimuli using psychopy functions
main_dir=os.getcwd()
image_dir=os.path.join(main_dir,'images')

stimuli = ['face01.jpg', 'face02.jpg','face03.jpg','face04.jpg', 'face05.jpg','face06.jpg','face07.jpg', 'face08.jpg','face09.jpg', 'face10.jpg']

fixation = visual.TextStim(win, text="+")

#=====================
#START EXPERIMENT
#=====================
#-present start message text
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
    block_stxt.draw()
    win.flip()
    event.waitKeys()
    
    #-randomize order of trials here 
    np.random.shuffle(stimulus)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================
    #-for loop for nTrials *
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image = visual.ImageStim(win, units="pix", size=(400,400))
        
        #====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        fixation.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(2.0)
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time(stimulus duration)
        core.wait(2.0)
        
        #-draw end trial 
        block_etxt.draw()
        #-flip window
        win.flip()
        #-wait time(stimulus duration)
        core.wait(2.0)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()