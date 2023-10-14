import board
import neopixel
from ledPixelsPico import *

nPix = 30

pix = ledPixels(nPix, board.GP15)

pix.rainbow()
