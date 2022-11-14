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

