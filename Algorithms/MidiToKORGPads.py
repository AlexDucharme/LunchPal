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
def MidiToKORGPads(LunchPal):
    channels = input('Select MIDI channels, Ex. 2,4,5 : ')
    channels = channels.split(",")
    print("")
    try:
        # Basic CC Control
        # Transfering Note and velocity into X and Y value for the KAOSSILATOR PRO
        # WE NEED TO SEND MIDI DATA TO KAOS ON CHANNEL 0, OTHER CHANNEL DON'T SEEMS TO WORK 
        def send_note_to_kaoss(Val, Velo, output):
            msg_out_x = mido.Message('control_change', channel=0, control=12, value=Val)
            msg_out_y = mido.Message('control_change', channel=0, control=13, value=Velo)            
            # print("[OUT] - "+str(msg_out_x))
            # print("[OUT] - "+str(msg_out_y))
            output.send(msg_out_x)
            output.send(msg_out_y)
        #Never ending loop to read and write MIDI msg
        while True:
            line = 1 #Loop counter for printing puspose
            #Loop on each MIDI input(s) of the passed LunchPal Object
            for tmp_input in LunchPal.INPUTS:
                #Open source
                with mido.open_input(tmp_input) as inport:
                    #Read all MIDI msg and print it
                    #using the line counter to print repetitivly on the same lines
                    for msg in inport:
                        #We are listening only at the channels selected
                        if str(msg.channel) in channels :
                            for out in LunchPal.OUTPUTS :  
                                midi_output = mido.open_output(out)
                                try:   
                                    # NOTE ON ------------------                  
                                    if (msg.type == 'note_on'):
                                        msg_on = mido.Message('control_change', channel=0, control=92, value=127, time=0)
                                        midi_output.send(msg_on)
                                        send_note_to_kaoss(msg.note, msg.velocity, midi_output)
                                        if line >= 7:
                                            print("\r\033[7A", end="") #Go back 7 lines
                                            print("[IN] - "+str(msg))
                                            line = 1
                                        else :    
                                            print("[IN] - "+str(msg))
                                            line += 1
                                    # NOTE OFF ------------------
                                    elif (msg.type == 'note_off'):
                                        msg_off = mido.Message('control_change', channel=0, control=92, value=0, time=0)
                                        midi_output.send(msg_off)
                                        if line >= 7:
                                            print("\r\033[7A", end="") #Go back 7 lines
                                            print("[IN] - "+str(msg))
                                            line = 1
                                        else :    
                                            print("[IN] - "+str(msg))
                                            line += 1
                                    else :
                                        pass
                                except:
                                    try:
                                        if (msg.control > 0):
                                            if line >= 7:
                                                print("\r\033[7A", end="") #Go back 7 lines
                                                print("[NOT SEND - IN] - "+str(msg))
                                                line = 1
                                            else :    
                                                print("[NOT SEND - IN] - "+str(msg))
                                                line += 1                                
                                    except Exception as e:
                                        print(e)
                                        pass
                        else :
                            #Pas dans la liste des channels
                            pass
    except KeyboardInterrupt :
        pass
    return 0 

#----------------------------------------#
# Execute the function when this file is call
#----------------------------------------#
if __name__ == '__main__':
    MidiToKORGPads(sys.argv[1])