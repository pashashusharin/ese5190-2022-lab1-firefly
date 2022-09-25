import board
import neopixel
import usb_hid
import time
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_apds9960.apds9960 import APDS9960

#setup neopixel led
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

#set up i2c connection
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)

#Enable sensors
apds.enable_proximity = True
apds.enable_color = True
apds.enable_gesture = True

#set color integration time:
apds.color_integration_time = 2

#Set up mouse and Keyboard
m = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

c_old = 0
red = True #(exit condition)
while red == True:
    #Color reading
    r, g, b, c = apds.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'. format(r, g, b, c))
    print('Brightness: {0}'. format(c))
    
    #Print i with the change of brightness 
    if c > c_old:
        kbd.send(Keycode.I)
    elif c < c_old:
        kbd.send(Keycode.BACKSPACE)
    time.sleep(0.05)
    
    #Abort the while loop and print r when sensor sees red color 
    if r > 20:
        kbd.send(Keycode.R)
        red = False
    
    print('r: {0}'. format(r))
    print('B: {0}'. format(b))
    c_old = c
    
    #Move mouse curser left to write when brightness changes
    #m.move(c-64, 0, 0)






