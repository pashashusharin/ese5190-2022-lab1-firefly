import board
import neopixel
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
apds.color_integration_time = 4

while True:
    #Color reading
    r, g, b, c = apds.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'. format(r, g, b, c))
    print('Brightness: {0}'. format(c))

    #light up the led if the brightness is high
    if c > 100:
        pixels.fill((255, 0, 0))
    else:
        pixels.fill((0,0,0))
