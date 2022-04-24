# LunchPal
```bash
   #---------------------------------#
        ╦  ┬ ┬┌┐┌┌─┐┬ ┬╔═╗┌─┐┬  
        ║  │ │││││  ├─┤╠═╝├─┤│  
        ╩═╝└─┘┘└┘└─┘┴ ┴╩  ┴ ┴┴─┘               
    #-------------------------------#
```
Becasue MIDI == Lunch Time !

LunchPal is a small set of python class and functions, base on mido, to experiment with MIDI signals processing algorithms. This project was born because I needed to find easy way to convert MIDI notes from any inputs into a series of control changes (CC) for the Korg KP3 and the KAOSSILATOR Pro. While I was exploring this problem, I was wondering : what if I want to test different algorithms? Or what if I want to have multiple virtual MIDI "bots" at the same time? This is why I made the LunchPal, to be able manage multiple MIDI "bots" and experiment with their processing of the MIDI signal.

## How it works?
You first sketch a LunchPal, which means giving it a name and choosing its MIDI input port, output port and channels. You then write some functions to handle the MIDI signals by your LunchPal. Finaly, you "summon" your LunchPal with the chosen algorithm.

## Environnement
I create and run this script on ubuntu 19.10 and use the gnome-terminale for with subprocess. To change the terminal used go in the LunchPal_CLI.py file : 
```Python3
# DEFAULT TERMINAL TOOL
TERMINAL = "gnome-terminal"  #<-- change this line
```

## Dependencies
I use python3 with mido and subprocess and you should be able to install them easely like this :
```Python3
pip3 install mido
```

## How to run
Run the tool, create a new LunchPal and summon it!
```
Python3 LunchPal_CLI.py
```

### The Main Menu
```bash
               -- [ OPTIONS ] --

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
