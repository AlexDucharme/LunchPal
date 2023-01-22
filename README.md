# LunchPal
```bash
   #---------------------------------#
        ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
        ║  │ │││││  ├─┤╠═╝├─┤│  
        ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
    #-------------------------------#
```
**Becasue MIDI == Lunch Time !**  
LunchPal is a small set of python class and functions, to experiment with MIDI signals processing algorithms.  
This project was born because I needed to find easy way to convert MIDI notes from any inputs into a series of control changes (CC) for the Korg KP3 and the KAOSSILATOR Pro. While I was exploring this problem, I was wondering : what if I want to test different algorithms? Or what if I want to have multiple virtual MIDI "bots" at the same time? This is why I made the LunchPal, to be able manage multiple MIDI "bots" and experiment with their processing of the MIDI signal.

## How it works?
### 1- Sketch a LunchPal 
Sketch a LunchPal with the CLI or your own code, wich will generate a .lchPal file. This .lchPal file is a pickle of your LunchPal class/object created.  
#### With the CLI : 
```bash
cd path/to/lunchpaldir/
Python3 LunchPal_CLI.py
### Select the '1' option
```
#### With the Python library : 
```Python3
#Import LunchPal class
from LunchPal import *

#Create a empty Pal
Pal = LunchPal()

#Giving it a name
Pal.NAME = "Pal's_Name"

#Pal Dictionaris = { MIDI_DEVICE_NAME : CHANNEL LIST }
#Channels are not use directly in the LunchPal right now

#Setup for MIDI INTPUT
Pal.INPUTS = {
    "Midi Through:Midi Through Port-0 14:0" : []
}
#Setup for MIDI OUTPUT
Pal.OUTPUTS = {
    "KP3:KP3 KP3 _ SOUND 24:0" : []
}

#Save Pal (pickle file .lchPal)
Pal.saveLunchPal()
```
### 2- Create Algorithm
You then write some functions to handle the MIDI signals comming in and out of your LunchPal.  
#### HelloWorld exemple :
```Python3
#----------------------------------------#
#           BASE SETUP
#----------------------------------------#
"""
You can import any module you like to play with MIDI or
any other audio/visual processing.
"""
import sys, os
import mido #mido MIDI package
sys.path.append("../") #Add path for the LunchPal.py file
from LunchPal import Algorithmz #Import Algorithmz decorator

#----------------------------------------#
#           ALGORITHM
#----------------------------------------#
@Algorithmz
def helloworld(LunchPal):
    """
    Simply pass a LunchPal object to a function to be able
    to access the LunchPal object attribute, for exemple :
        - LunchPal.NAME
        - LunchPal.INPUTS
        - LunchPal.OUTPUTS
    """
    print("Hello World - "+LunchPal.NAME)
    input("Press ENTER to close this windows")

#----------------------------------------#
# Execute the function when this file is call
#----------------------------------------#
if __name__ == '__main__':
    """
    Don't forget to assign sys.argv[1] as your LunchPal
    object and run your algorithm when when __name__ == __main__
    """
    helloworld(sys.argv[1])
```
### 3- Summoning your LunchPal
Finaly, you "summon" your LunchPal with the chosen algorithm with the CLI or directly in command line.  
#### With the CLI : 
```bash
cd path/to/lunchpaldir/
Python3 LunchPal_CLI.py
### Select the '!' option
```
#### Command line : 
```bash
#This will launch the Exemple LunchPal with the helloworld algorithm
cd path/to/algorithms/
Python3 helloworld Exemple.lunchPal
```


## Environnement
I create and run this script on ubuntu 20.04 and use the gnome-terminale with subprocess. To change the terminal used when summoning a pal with the LunchPal_CLI.py : 
```Python3
# DEFAULT TERMINAL TOOL
TERMINAL = "gnome-terminal"  #<-- change this line
```

## Dependencies
```Python3
mido
subprocess
pickle
```

## The CLI Main Menu
```bash
           #---------------------------------#
                ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
                ║  │ │││││  ├─┤╠═╝├─┤│  
                ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
            #-------------------------------#

       [1] - Sketch a new LunchPal
       [2] - List all LunchPal 
       [3] - List all Algorithms
       [!] - Summon a LunchPal
       [q] - QUIT or Ctrl+c

```
[1] Chose this to **create a new LunchPal**  
[2] Choose this to **show all LunchPal** created  
[3] Chose this to **show all Algorithme** availaible  
[!] Choose this to **summon a LunchPal**  
[q] **QUIT** 

## Listing MIDI devices name with mido
```Python3
#Import mido lib
import mido

#Print all input MIDI devices
print(mido.get_input_names())

#Print all output MIDI devices
print(mido.get_output_names())
```
