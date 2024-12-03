"""
Created by: Ella An
Created on: Nov 2024
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel
from time import sleep

# setup
np = neopixel.NeoPixel(pin16, 4)

while True:
    # turn green on
    np[0] = (0, 0, 0)
    np[1] = (0, 0, 0)
    np[2] = (0, 128, 0)
    np[3] = (0, 0, 0)
    np.show()

    sleep(1)

    # turn yello on
    np[0] = (0, 0, 0)
    np[1] = (255, 255, 0)
    np[2] = (0, 0, 0)
    np[3] = (0, 0, 0)
    np.show()

    sleep(1)

    # turn red on
    np[0] = (255, 0, 0)
    np[1] = (0, 0, 0)
    np[2] = (0, 0, 0)
    np[3] = (0, 0, 0)
    np.show()

    sleep(1)

    # turn it all off
    np[0] = (0, 0, 0)
    np[1] = (0, 0, 0)
    np[2] = (0, 0, 0)
    np[3] = (0, 0, 0)
    np.show()
