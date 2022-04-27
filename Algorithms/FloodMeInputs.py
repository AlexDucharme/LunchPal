#----------------------------------------#
#           BASE SETUP
#----------------------------------------#
import sys, os
import mido #mido MIDI package
sys.path.append("../") #Add path for the LunchPal.py file
from LunchPal import Algorithmz #Import Algorithmz decorator

#----------------------------------------#
#           ALGORITHM
#----------------------------------------#
@Algorithmz
def FloodMeInput(LunchPal):
    try:
        #Never ending loop to read and write MIDI msg
        while True:
            line = 1 #Counter to loop the printing of MIDI msg on 7 lines
            #Loop on each MIDI sources of the passed LunchPal Object
            for i in range (0, len(LunchPal.SOURCE_IN)):
                #Open source
                with mido.open_input(LunchPal.SOURCE_IN[i]) as inport:
                    #Read all MIDI msg and print it
                    for msg in inport:
                        if line >= 7:
                            print("\r\033[7A", end="") #Go back 7 lines
                            print(msg)
                            line = 1
                        else :    
                            print(msg)
                            line += 1
    except KeyboardInterrupt :
        pass
    return 0 

#----------------------------------------#
# Execute the function when this file is call
#----------------------------------------#
if __name__ == '__main__':
    FloodMeInput(sys.argv[1])