from LunchPal import *
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
        
        algorithmName = sys.argv[1]
        Pal = LunchPal()
        Pal.loadLunchPal(LunchPalName)
        Pal.LunchPalInfo()
        Pal.summon(algorithmName, func)
   
    return inner

##################################################################################################################
##################################################################################################################
'''
 ▄▄▄       ██▓      ▄████  ▒█████   ██▀███   ██▓▄▄▄█████▓ ██░ ██  ███▄ ▄███▓
▒████▄    ▓██▒     ██▒ ▀█▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒▓██░ ██▒▓██▒▀█▀ ██▒
▒██  ▀█▄  ▒██░    ▒██░▄▄▄░▒██░  ██▒▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░▒██▀▀██░▓██    ▓██░
░██▄▄▄▄██ ▒██░    ░▓█  ██▓▒██   ██░▒██▀▀█▄  ░██░░ ▓██▓ ░ ░▓█ ░██ ▒██    ▒██ 
 ▓█   ▓██▒░██████▒░▒▓███▀▒░ ████▓▒░░██▓ ▒██▒░██░  ▒██▒ ░ ░▓█▒░██▓▒██▒   ░██▒
 ▒▒   ▓▒█░░ ▒░▓  ░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓    ▒ ░░    ▒ ░░▒░▒░ ▒░   ░  ░
  ▒   ▒▒ ░░ ░ ▒  ░  ░   ░   ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░    ░     ▒ ░▒░ ░░  ░      ░
  ░   ▒     ░ ░   ░ ░   ░ ░ ░ ░ ▒    ░░   ░  ▒ ░  ░       ░  ░░ ░░      ░   
      ░  ░    ░  ░      ░     ░ ░     ░      ░            ░  ░  ░       ░   
'''                                                                            

@Algorithmz
def Flood_Me_Input_Ch_0(LunchPal):
    try:
        while True:
            line = 1
            with mido.open_input(LunchPal.SOURCE_IN[0]) as inport:
                for msg in inport:
                    if line >= 7:
                        print("\r\033[7A", end="")
                        print(msg)
                        line = 1
                    else :    
                        print(msg)
                        line += 1
    except KeyboardInterrupt :
        pass
    return 0 


@Algorithmz
def Flood_Me_Input_All(LunchPal):
    try:
        while True:
            line = 1
            for i in range (0, len(LunchPal.SOURCE_IN)):
                with mido.open_input(LunchPal.SOURCE_IN[i]) as inport:
                    for msg in inport:
                for msg in inport:
                    if line >= 7:
                        print("\r\033[7A", end="")
                        print(msg)
                        line = 1
                    else :    
                        print(msg)
                        line += 1
    except KeyboardInterrupt :
        pass
    return 0 

###########################################################################################
###########################################################################################
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
def getAlgoList():
    algoList = []
    for i in dir(sys.modules[__name__]):
        if i.startswith("__"):
            break
        elif i == "LunchPal" or i == "Algorithmz" or i == 'LUNCHPALL_FILE':
            pass
        else :
            algoList.append(i)
    return algoList
    #print(algoList)

def selectAlgorithme():
    algoList = getAlgoList()
    xx = 1
    print("Choose Algorithm :")
    for algo in algoList:
        print("["+str(xx)+"] - "+str(algo))
        xx += 1
    selectedAlgo = input('[ --> ]  ')
    return algoList[int(selectedAlgo)-1]

# To be able to call a function from the command line
if __name__ == '__main__':
    '''
    sys.argv[1] == Name of decorated function (Algorithmz)
    sys.argv[2] == LunchPal's name to be used
    '''
    try: # To run a specific function with a LunchPal object from command line
        globals()[sys.argv[1]](sys.argv[2])
    except:
        pass
