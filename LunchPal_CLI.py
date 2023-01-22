import sys
import os
import time
import mido
import pickle

##########################################################################################
'''
   #---------------------------------#
        ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
        ║  │ │││││  ├─┤╠═╝├─┤│  
        ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
    #-------------------------------#
Becasue MIDI == Lunch Time !
LunchPal class to create object that are pass to MIDI procesing algorithm.
You can setup, save and load a LunchPal with the method setupLunchPal(), saveLunchPal()
and loadLunchPal().
You can display the LunchPal attribute with the LunchPalInfo() method.
At creation, the atributes of a LunchPal object are all empty.
'''

LOGO = '''           #---------------------------------#
                ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
                ║  │ │││││  ├─┤╠═╝├─┤│  
                ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
            #-------------------------------#'''

class LunchPal(object):

        def __init__(self):
            self.NAME = ""
            self.NBR_SOURCE_IN = 0
            self.INPUTS = {}
            self.NBR_SOURCE_OUT = 0
            self.OUTPUTS = {}


        def setName(self):
            self.NAME = input("Enter a name for your new LunchPal :")
#
        def setSource(self, inOut):
            nbr_source = input("How many "+inOut+" source ? : ")
            if nbr_source in "1234567890":
                if inOut == "input":
                    self.NBR_SOURCE_IN = nbr_source
                elif inOut == "output":
                    self.NBR_SOURCE_OUT = nbr_source
                if nbr_source == 0:
                    if inOut == "input":
                        self.INPUTS["NON"] = []
                    elif inOut == "output":
                        self.OUTPUTS["NON"] = []
                #Initialisation of sources dictionary, at first it was for channel
                #but I disable sont channel feature for now
                else:
                    for i in range(0, int(nbr_source)):
                        if inOut == "input":
                            source = self.chooseSource(inOut)
                            self.INPUTS[source] = []
                        elif inOut == "output":
                            source = self.chooseSource(inOut)
                            self.OUTPUTS[source] = []
            else :
                print("[!] - Invalid entry !")
                self.setSource(str(inOut))

        # Should be define in the algorythm for a better fluidité
        # def setChannel(self, inOut):
        #     if inOut == "input":
        #         for k in self.INPUTS:
        #             print("Enter "+inOut+" channel for "+k+", separeted by coma.")
        #             print("EXEMPLE : 2,3,4,6")
        #             channels = input('[ --> ]  ')
        #             self.INPUTS[k] = channels.split(",")
        #     elif inOut == "output":
        #         for k in self.OUTPUTS:
        #             print("Enter "+inOut+" channel for "+k+", separeted by coma.")
        #             print("EXEMPLE : 2,3,4,6")
        #             channels = input('[ --> ]  ')
        #             self.OUTPUTS[k] = channels.split(",")
        
        #Channel selections when creating a pal is disable
        def setupLunchPal(self):
            self.NAME = input("MIDI Friend name [ --> ]  ")
            self.setSource("input")
            # if self.NBR_SOURCE_IN != 0:
            #     self.setChannel("input")
            # else:
            #     self.INPUTS["NON"] = []
            
            self.setSource("output")
            # if self.NBR_SOURCE_OUT != 0:
            #     self.setChannel("output")
            # else:
            #     self.OUTPUTS["NON"] = []


        def saveLunchPal(self):
            try:
                pickle.dump(self, open("Pals/"+self.NAME+".lchPal", "wb" ))
            except :
                pickle.dump(self, open("Pals/"+self.NAME+".lchPal", "w" ))

        def loadLunchPal(self, LunchPalName):
            tmp_self = pickle.load(open("../Pals/"+LunchPalName, "rb" ))
            self.NAME = tmp_self.NAME
            self.NBR_SOURCE_IN = tmp_self.NBR_SOURCE_IN
            self.INPUTS = tmp_self.INPUTS
            self.NBR_SOURCE_OUT = tmp_self.NBR_SOURCE_OUT
            self.OUTPUTS = tmp_self.OUTPUTS

        
        def LunchPalInfo(self):
            print(LOGO)
            print("")
            print("[NAME] : "+self.NAME)
            for k in self.OUTPUTS:
                print("[MIDI OUTPUT] : "+str(k))
            for k in self.INPUTS:
                #print("[!] MIDI INPUT : \n[*] - "+str(k)+" - CHANNEL(S): "+str(self.INPUTS[k]))
                print("[MIDI INPUT] : "+str(k))
            print("\n                 #---------------------#")


        #Function use to select MIDI sources, IN or OUT
        def chooseSource(self, inOut):
            # Variable settings
            if inOut == "input":
                source = "input"
                nbr_source_device = len(mido.get_input_names())
                device_list = mido.get_input_names()
            elif inOut == "output":
                source = "output"
                nbr_source_device = len(mido.get_output_names())
                device_list = mido.get_output_names()
            #--------------------   
            print("[ "+self.NAME+" ] - -  CHOOSE "+source.upper()+" SOURCE(S) - - ")
            #--------------------
            # Display all sources
            xx = 1   # Counter, ID
            for device in device_list :
                print("["+str(xx)+"] " + device)
                xx = xx + 1
            print("["+str(xx)+"] NON")
            #--------------------
            #Choice of input (User will input source ID number)
            CHOICE= input('[ --> ]  ')
            print(CHOICE)
            if CHOICE in "1234567890" and int(CHOICE) <= xx:
                try:
                    if (int(CHOICE) <= nbr_source_device):
                        CHOICE = device_list[int(CHOICE)-1]
                        return CHOICE
                    elif (int(CHOICE) == xx) :
                        return "NON"
                    else:
                        print("\n[!] - No "+source+" port selected")
                except Exception as e:
                    print(e)
            else :
                print("[!] - Invalid entry !")
                self.chooseSource(str(inOut))


        # Methode to summon a LunchPal
        def summon(self, algorithmeName, func):
            try:
                print("\n[~~~] - Lunching "+str(algorithmeName).upper()+" algorithm ...")
                return func(self) 
            except Exception as e:
                print("Error lunching algorithm, sorry about that ... .. .")
                print(e)
                pass           


##################################################################################################################
##################################################################################################################
'''
▓█████▄ ▓█████  ▄████▄   ▒█████   ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░  ░    ░   ░        ░ ░ ░ ▒    ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
   ░       ░  ░░ ░          ░ ░     ░           ░  ░            ░ ░     ░     
 ░             ░                                                              
Decorator function use for quickly prototyping MIDI processing algorithm
'''

def Algorithmz(func):
    def inner(LunchPalName):
        Pal = LunchPal()
        Pal.loadLunchPal(LunchPalName)
        Pal.LunchPalInfo()
        Pal.summon(sys.argv[0], func)  
    return inner



##################################################################################################################
# Stuff to do when imported
if __name__ == '__main__':
    pass
