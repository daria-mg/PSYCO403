#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event, data

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os, random 

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir, 'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, 'images')

#-check that these directories exist
if not os.path.isdir(image_dir):
    raise Exception ("Could not find the path.")
if not os.path.isdir(data_dir):
    raise Exception ("Could not find the path.")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials= 10
nBlocks= 2

#stimulus names (and stimulus extensions, if images) *
stim_name = "face"
stim_ext = ".jpg"

#stimulus properties like size, orientation, location, duration *
s_size = (200, 200)
s_orientation = "landscape"
s_location = [0,0]
s_duration = 1

#start message text *
start_msg = "Welcome to the experiment!"
print(start_msg)

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
pics = []
for index in range (1,11):
    if index < 10:
        pics.append(stim_name + "0" + str(index) + stim_ext)
    else:
        pics.append(stim_name + str(index) + stim_ext)

for pic in pics:
    if pic in os.listdir(image_dir):
        print(pic + "was found!")
    else:
        raise Exception ("The image lists don't match up. An image or more don't exist.")

#-create counterbalanced list of all conditions *
zippedlist = list(zip(pics, nTrials))

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
corResponse = []
#create an empty list for participant responses (e.g., "on this trial, response was a X") *
parResponse = []
#create an empty list for response accuracy collection (e.g., "was participant correct?") *
accuracyList = []
#create an empty list for response time collection *
RTlist = []
#create an empty list for recording the order of stimulus identities *
stimIdent = []
#create an empty list for recording the order of stimulus properties *
stimProperties = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(nBlocks):
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(zippedlist)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================
    #-for loop for nTrials *
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment