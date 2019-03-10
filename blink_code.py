from microbit import *


while True:
    display.set_pixel(0,0,9)
    display.set_pixel(4,4,9)
    sleep(1000)
    display.set_pixel(0,0,1)
    display.set_pixel(4,4,1)
    sleep(1000)