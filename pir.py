import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.setup(6, GPIO.OUT)
#GPIO.output(6, 0)

#GPIO.setup(19, GPIO.OUT)
#GPIO.output(19, 0)

GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 0)

try:
       while True:
           #GPIO.output(6, GPIO.input(22))
           #GPIO.output(19, GPIO.input(22))
           GPIO.output(21, GPIO.input(22))#lights led and sounds buzzer
           
           if (GPIO.input(22) == 1):
              mylcd.lcd_display_string("Intruder alert!!", 1)
           else:
              mylcd.lcd_clear()
              

except KeyboardInterrupt:
    GPIO.cleanup()
