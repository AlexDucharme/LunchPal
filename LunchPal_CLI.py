from Algorithms import *
import subprocess

'''
   #---------------------------------#
        ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
        ║  │ │││││  ├─┤╠═╝├─┤│  
        ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
                        	v1.0
    #-------------------------------#
Becasue MIDI == Lunch Time !
Command Line Interface to create, view and summon LunchPal
If your are not using gnome terminale your should edit the TERMINAL variable
'''
# DEFAULT TERMINAL TOOL
TERMINAL = "gnome-terminal"

def printMainMenu():
    with open("Menu.txt") as menu:
        for line in menu:
            print(line, end="\r")

def listAlgorithme():
    print(" - - ALGORITHMES - -")
    for i in getAlgoList():
        print("\t - "+i)
    press_ent = input('Press Enter to continue!')

def newLunchPal():
    newPal = LunchPal()
    newPal.setupLunchPal()
    newPal.saveLunchPal()

def summonLunchPal():
    selectedLunchPal = selectLunchPal()
    selectedAlgorithm = selectAlgorithme()
    cmd = [TERMINAL, "--", "python3", "Algorithms.py", selectedAlgorithm, selectedLunchPal]
    subprocess.run(cmd)

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

if __name__ == '__main__':
    main()
