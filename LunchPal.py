import sys
from os import path
import time
import mido

##########################################################################################
'''
   #---------------------------------#
        ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
        ║  │ │││││  ├─┤╠═╝├─┤│  
        ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
                        	v1.0
    #-------------------------------#
Becasue MIDI == Lunch Time !
LunchPal class to create object that are pass to MIDI procesing algorithm.
You can setup, save and load a LunchPal with the method setupLunchPal(), saveLunchPal()
and loadLunchPal().
You can display the LunchPal attribute with the LunchPalInfo() method.
At creation, the atributes of a LunchPal object are all empty.
'''
LUNCHPALL_FILE = 'LunchPal.lst'

logo = '''   #---------------------------------#
        ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
        ║  │ │││││  ├─┤╠═╝├─┤│  
        ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
                        	v1.0
    #-------------------------------#'''

class LunchPal(object):

        def __init__(self):
            self.NAME = ""
            self.SOURCE_IN = []
            self.SOURCE_IN_INFO = []
            self.CHANNEL_IN = []
            self.SOURCE_OUT = []
            self.SOURCE_OUT_INFO = []
            self.CHANNEL_OUT = []

        def setName(self):
            self.NAME = input("Enter a name for your new LunchPal :")

        def setSource(self, inOut):
            nbr_source = input("How many "+inOut+" source ? : ")
            for i in range(0, int(nbr_source)):
                if inOut == "input":
                    source = self.chooseSource(inOut)
                    self.SOURCE_IN.append(source)
                    self.SOURCE_IN_INFO.append(source.split(':')[0])
                elif inOut == "output":
                    source = self.chooseSource(inOut)
                    self.SOURCE_OUT.append(source)
                    self.SOURCE_OUT_INFO.append(source.split(':')[0])
                
        def setChannel(self, inOut):
            print("Enter "+inOut+" channel to be used, separeted by coma.")
            print("EXEMPLE : 2,3,4,6")
            channels = input('[ --> ]  ')
            if inOut == "input":
                self.CHANNEL_IN = channels.split(",")
            elif inOut == "output":
                self.CHANNEL_OUT= channels.split(",")
        
        def setupLunchPal(self):
            self.NAME = input("MIDI Friend name [ --> ]  ")
            self.setSource("input")
            self.setChannel("input")
            self.setSource("output")
            self.setChannel("output")

        def saveLunchPal(self):
            with open(LUNCHPALL_FILE, 'a') as saveFile:
                saveFile.write(str(self.NAME+"|"+str(self.SOURCE_IN)+"|"+str(self.CHANNEL_IN)+"|"+str(self.SOURCE_OUT)+"|"+str(self.CHANNEL_OUT)+"|"+str(self.SOURCE_IN_INFO)+"|"+str(self.SOURCE_OUT_INFO)+"\n"))

        def loadLunchPal(self, LunchPalName):    
            with open(LUNCHPALL_FILE) as loadFile:
                for line in loadFile:
                    line = line.replace("['","").replace("']","").replace("'","").replace("\n","").split('|')
                    if line[0] == LunchPalName:
                        self.NAME = line[0]
                        self.SOURCE_IN = line[1].split(",")
                        self.SOURCE_IN_INFO = line[5].split(",")
                        self.CHANNEL_IN = line[2].split(",")
                        self.SOURCE_OUT = line[3].split(",")
                        self.SOURCE_OUT_INFO = line[6].split(",")
                        self.CHANNEL_OUT = line[4].split(",")
        
        def LunchPalInfo(self):
            print(logo)
            print("\n  -"+self.NAME+"-  ")
            for i in range(0,len(self.SOURCE_OUT_INFO)) :
                print("[!] MIDI OUTPUT : "+str(self.SOURCE_OUT_INFO[i])+" - CHANNEL OUT : ", end="")
                for l in range(0,len(self.CHANNEL_OUT)) :
                    print(str(self.CHANNEL_OUT[l]), end=" ")
            #print("\n")
            for i in range(0,len(self.SOURCE_IN_INFO)) :
                print("\n[!] MIDI INPUT : "+str(self.SOURCE_IN_INFO[i])+" - CHANNEL INPUT : ", end="")
                for l in range(0,len(self.CHANNEL_IN)) :
                    print(str(self.CHANNEL_IN[l]), end=" ")
            #print("\n")

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
            print("["+str(xx)+"] NONE")
            #--------------------
            #Choice of input (User will input source ID number)
            CHOICE= input('[ --> ]  ')
            try:
                if (int(CHOICE) <= nbr_source_device):
                    CHOICE = device_list[int(CHOICE)-1]
                    return CHOICE
                elif (int(CHOICE) == nbr_source_device+1) :
                    return "NONE"
                else:
                    print("\n[!] - No "+source+" port selected")
            except:
                print("[!] - Invalid entry !")

        #Opening the OUT port
        def openOUTPUTport(self):
            print("\n[*] - Opening port ... .. .")
            for i in range (0, len(self.SOURCE_OUT)):
                try:
                    globals()['port'+str(i+1)] = mido.open_output(self.SOURCE_OUT[i])
                    print("[*] - port"+str(i+1)+" is open with " + str(self.SOURCE_OUT_INFO[i]))
                    time.sleep(0.5)
                except:
                    if self.SOURCE_OUT[i] == "None":
                        print("[!] - No device specified for port"+str(i+1)+" (None)")
                    else:
                        print("[!] - port"+str(i+1)+" failed to open with " + self.SOURCE_OUT_INFO[i])
                    time.sleep(0.5)

        # Methode to summon a LunchPal
        def summon(self, algorithmeName, func):
            self.openOUTPUTport()
            print("[*] - Lunching "+str(algorithmeName).upper()+" algorithm ... .. .\n")
            print("#-==-#-==-#-==-#-==-#-==-#-==-#-==-#-==-#-==-#\n")
            try:
                return func(self) 
            except:
                print("Error lunching algorithm, sorry about that ... .. .")
                pass           

##########################################################################################
##########################################################################################
'''
 ▒█████  ▄▄▄█████▓ ██░ ██ ▓█████  ██▀███  
▒██▒  ██▒▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒██░  ██▒▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒██   ██░░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
░ ████▓▒░  ▒██▒ ░ ░▓█▒░██▓░▒████▒░██▓ ▒██▒
░ ▒░▒░▒░   ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░ ▒ ▒░     ░     ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ▒    ░       ░  ░░ ░   ░     ░░   ░ 
    ░ ░            ░  ░  ░   ░  ░   ░   
Other function for use with the CLI
'''

def printListLunchPal():
    with open(LUNCHPALL_FILE) as loadFile:
        for line in loadFile:
            line = line.replace("['","").replace("']","").replace("'","").replace("\n","").split('|')
            print("------ [ "+line[0]+" ] ---------------------------------------------------")
            for i in range(0,len(line[6].split(','))) :
                print("[!] MIDI OUTPUT : "+str(line[6].split(',')[i])+" - CHANNEL OUT : ", end="")
                for l in range(0,len(line[2].split(','))) :
                    print(str(line[2].split(',')[l]), end=" ")
            for i in range(0,len(line[5].split(','))) :
                print("\n[!] MIDI INPUT : "+str(line[5].split(',')[i])+" - CHANNEL INPUT : ", end="")
                for l in range(0,len(line[4].split(','))) :
                    print(str(line[4].split(',')[l]), end=" ")
            print("\n")


def selectLunchPal():
    with open(LUNCHPALL_FILE) as loadFile:       
        listLunchPal = []
        for line in loadFile:
            line = line.replace("['","").replace("']","").replace("'","").replace("\n","").split('|')
            listLunchPal.append(str(line[0]))
    xx = 1    
    print("Choose LunchPal :")
    for lunchPal in listLunchPal:    
        print("["+str(xx)+"] - "+lunchPal)
        xx += 1
    selectedLunchPal = input('[ --> ]  ')
    return listLunchPal[int(selectedLunchPal)-1]

# Stuff to do when imported
if __name__ == '__main__':
    pass
