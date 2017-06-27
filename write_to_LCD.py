import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

name = input("What is your name?")

mylcd.lcd_display_string("Hello " + name, 1)
mylcd.lcd_display_string("How are you?", 2)
    
sleep(3)
mylcd.lcd_clear()


str_pad = " " * 16
my_long_string = "I finally got the Raspberry Pi to work!!"
my_long_string = str_pad + my_long_string

while True:
    for i in range (0, len(my_long_string)):
        lcd_text = my_long_string[i:(i+16)]
        mylcd.lcd_display_string(lcd_text,1)
        sleep(0.1)
        mylcd.lcd_display_string(str_pad,1)
        
