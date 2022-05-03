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