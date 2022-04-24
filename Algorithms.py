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
        
        Pal = LunchPal()
        Pal.loadLunchPal(LunchPalName)
        Pal.LunchPalInfo()

	# Devrait être une méthode de LunchPal
        # ex : openPort() 
        print("\n[ ! ] - Opening port ... .. .")
        for i in range (0, len(Pal.SOURCE_OUT)):
            try:
                globals()['port'+str(i+1)] = mido.open_output(Pal.SOURCE_OUT[i])
                print("[*] - port"+str(i+1)+" is open with " + str(Pal.SOURCE_OUT[i]))
                time.sleep(0.5)
            except:
                if Pal.SOURCE_OUT[i] == "None":
                    print("[*] - No device specified for port"+str(i+1)+" (None)")
                else:
                    print("[*] - port"+str(i+1)+" failed to open with " + Pal.SOURCE_OUT[i])
                time.sleep(0.5)
    
    # Devrait être une méthode de LunchPal
        # ex: summon() ou Lunch() ou LunchTime()
        print("[ ! ] - Lunching "+str(sys.argv[1]).upper()+" algorithm ... .. .\n")
        try:
            return func(Pal) 
        except:
            print("Error lunching algorithm, sorry about that ... .. .")
            pass
   
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
def Flood_Me_Input(LunchPal):
    try:
        while True:
            with mido.open_input(LunchPal.SOURCE_IN[0]) as inport:
                for msg in inport:
                    print(msg)
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
    print("Choose Algorithme :")
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
