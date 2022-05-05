from LunchPal import *
import subprocess
import os, sys

sys.path.append(str(os.getcwd()+"/Algorithms"))
'''
   #---------------------------------#
        ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
        ║  │ │││││  ├─┤╠═╝├─┤│  
        ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
    #-------------------------------#
Becasue MIDI == Lunch Time !
Command Line Interface to create, view and summon LunchPal
If your are not using gnome terminale your should edit the TERMINAL variable
'''
# DEFAULT TERMINAL TOOL
TERMINAL = "gnome-terminal"

# BASIC MENU
MENU = '''
       [1] - Sketch a new LunchPal
       [2] - List all LunchPal 
       [3] - List all Algorithms
       [!] - Summon a LunchPal
       [q] - QUIT or Ctrl+c
'''

# DEFAULT LUNCHPAL FILE
LUNCHPALL_FILE = 'LunchPal.lst'

def printMainMenu():
    print(LOGO)
    print(MENU)

def listAlgorithme():
    print("\n - - ALGORITHMES - -")
    for i in getAlgoList():
        print("--> "+i)
    print("- - - - - - - - - - -")
    press_ent = input('Press Enter to continue!')

def newLunchPal():
    newPal = LunchPal()
    newPal.setupLunchPal()
    newPal.saveLunchPal()

def summonLunchPal():
    algoPath = str(os.getcwd()+"/Algorithms")
    selectedLunchPal = selectLunchPal()
    selectedAlgorithm = selectAlgorithme()
    os.chdir(algoPath) # Change path to summon
    cmd = [TERMINAL, "--", "python3", selectedAlgorithm, selectedLunchPal]
    subprocess.run(cmd)
    os.chdir("..") # Come back


def main():
    main_loop = True
    while main_loop:
        printMainMenu()
        user_input = input('[Option] : ')
        if user_input not in ['1', '2', '3', '!', 'q']:
            pass
        else:
            if user_input == '1':
                newLunchPal()
            elif user_input == '2':
                printListLunchPal()
                press_ent = input('Press Enter to continue!')
            elif user_input == '3':
                listAlgorithme()
            elif user_input == '!':
                summonLunchPal()
            elif user_input == 'q':
                main_loop = False

def printListLunchPal():
    lchpal_list = []
    for f in os.listdir(str(os.getcwd()+"/Pals")):
        try:
            ext = f.split('.')[1]
            if ext == "lchPal":
                lchpal_list.append(f)
        except Exception as e:
            pass

    for pal in lchpal_list:
        print("[*] "+pal)


    # with open(LUNCHPALL_FILE) as loadFile:
    #     for line in loadFile:
    #         line = line.replace("['","").replace("']","").replace("'","").replace("\n","").split('|')
    #         print("------ [ "+line[0]+" ] ---------------------------------------------------")
    #         for i in range(0,len(line[6].split(','))) :
    #             print("[!] MIDI OUTPUT : "+str(line[6].split(',')[i])+" - CHANNEL OUT : ", end="")
    #             for l in range(0,len(line[2].split(','))) :
    #                 print(str(line[2].split(',')[l]), end=" ")
    #         for i in range(0,len(line[5].split(','))) :
    #             print("\n[!] MIDI INPUT : "+str(line[5].split(',')[i])+" - CHANNEL INPUT : ", end="")
    #             for l in range(0,len(line[4].split(','))) :
    #                 print(str(line[4].split(',')[l]), end=" ")
    #         print("\n")


def selectLunchPal():
    # with open(LUNCHPALL_FILE) as loadFile:       
    #     listLunchPal = []
    #     for line in loadFile:
    #         line = line.replace("['","").replace("']","").replace("'","").replace("\n","").split('|')
    #         listLunchPal.append(str(line[0]))
    lchpal_list = []
    for f in os.listdir(str(os.getcwd()+"/Pals/")):
        try:
            ext = f.split('.')[1]
            if ext == "lchPal":
                lchpal_list.append(f)
        except Exception as e:
            pass

    xx = 1    
    print("Choose LunchPal :")
    for pal in lchpal_list:
        print("["+str(xx)+"] - "+pal)
        xx += 1
    selectedLunchPal = input('[ --> ]  ')
    return lchpal_list[int(selectedLunchPal)-1]


def getAlgoList():
    algoList = []
    for f in os.listdir(str(os.getcwd()+"/Algorithms")):
        f.split('.')[0]
        algoList.append(f)
    return algoList


def selectAlgorithme():
    algoList = getAlgoList()
    xx = 1
    print("\nChoose Algorithm :")
    for algo in algoList:
        print("["+str(xx)+"] - "+str(algo))
        xx += 1
    selectedAlgo = input('[ --> ]  ')
    return algoList[int(selectedAlgo)-1]


if __name__ == '__main__':
    main()