Code for LED lamps.


# Requirements:
* Raspberry Pi Pico W
* Quick setup for CircuitPython v8: 
    * Install CircuitPython (next section).
    * Copy all files in this repository onto the Pico.
    * Bob's your uncle.

# Installation
## Install CircuitPython
Download and copy the appropriate CircuitPython file (version 8) to the Raspberry Pi Pico W:
* For Pico W: https://circuitpython.org/board/raspberry_pi_pico_w/

The Pico will rename itself CIRCUITPI

## Copy files
* Copy files and folders from this repository onto the Raspberry Pi.
    * Note Sources:
        * neopixel.mpy: https://circuitpython.org/libraries
        * ledPixelsPico.py: https://github.com/lurbano/ledPixelsPico
* The Pico will run the code.py file by default. 
    * This program assumes you have a 30 pixel array (at GPIO15) and a touch sensor (at GPIO16).
    * It will run a rainbow pattern that turns on and off when you touch the touch sensor.

## A lot of the files aren't needed and are probably duplicates with different names but I an WAY too lazy to go through all of that, code.py runs by default and works for me tho

