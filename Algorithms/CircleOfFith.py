#-----------------------------------------------------#
#           BASE SETUP
#-----------------------------------------------------#
import sys, os
import mido #mido MIDI package
sys.path.append("../") #Add path for the LunchPal.py file
from LunchPal import Algorithmz #Import Algorithmz decorator

import time
import random

#-----------------------------------------------------#
#  Function to get the next val on the CircleOf Fith
#-----------------------------------------------------#
def GetCircleNote(MidiNote, UpDown=True):
    #Val declaration
    NextNote = 0
    basenote = MidiNote % 12
    # Go up or down the circle
    if UpDown :
        if basenote >= 7 :
            NextNote = MidiNote - 7
        else :
            NextNote = MidiNote + 5
    else :
        if basenote >= 7 :
            NextNote = MidiNote + 7
        else :
            NextNote = MidiNote - 5
    # Return the next note val
    return NextNote

#-----------------------------------------------------#
#           ALGORITHM
#-----------------------------------------------------#
@Algorithmz
def CircleOfFith(LunchPal):
    try:
        #Never ending loop to read and write MIDI msg
        while True:
            line = 1 #Loop counter for printing puspose
            #Loop on each MIDI input(s) of the passed LunchPal Object
            for k in LunchPal.INPUTS:
                #Open source
                with mido.open_input(k) as inport:
                    #Read all MIDI msg and print it
                    #using the line counter to print repetitivly on the same lines
                    for msg in inport:
                        #Randomize UpDown for the next note
                        rand_int = random.randint(0,1)
                        for out in LunchPal.OUTPUTS :  
                            midi_output = mido.open_output(out)
                            #Check if it's a note_off
                            if (msg.type == 'note_off'):
                                #print("note_off")
                                msg_off = mido.Message('note_off', channel=msg.channel, note=GetCircleNote(msg.note), velocity=msg.velocity, time=0)
                                midi_output.send(msg_off)
                            # If it's a note_on
                            elif (msg.type == 'note_on'):
                                #for i in range(0,rand_int) :                       
                                #New midi msg
                                # new_note = GetCircleNote(msg.note)+(i*12)
                                new_note = GetCircleNote(msg.note, UpDown=rand_int)
                                NewMidiMsg = mido.Message('note_on',channel=msg.channel, note=new_note, velocity=msg.velocity, time=0)
                                if line >= 7:
                                    print("\r\033[7A", end="") #Go back 7 lines
                                    midi_output.send(NewMidiMsg)
                                    print("Note in : "+str(msg.note)+" Note out : "+str(new_note))
                                    line = 1
                                else :    
                                    midi_output.send(NewMidiMsg)
                                    print("Note in : "+str(msg.note)+" Note out : "+str(new_note))
                                    line += 1
                                    #time.sleep(1)
    except KeyboardInterrupt :
        pass
    return 0 

#-----------------------------------------------------#
# Execute the function when this file is call
#-----------------------------------------------------#
if __name__ == '__main__':
    CircleOfFith(sys.argv[1])