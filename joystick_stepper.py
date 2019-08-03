#!/usr/bin/python

#!/usr/bin/env python

import os, sys, pygame 
from pygame import locals
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# set the delay between steps
stepDelay = 0.002

# set up motor 1
GPIO.setup(8, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(8, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

# set up motor 2
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)


os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

pygame.joystick.init() # main joystick device system

deadZone = 0.6 # make a wide deadzone
m1 = 0 # motor 1 (1 = forward / 2 = backwards)
m2 = 0 # motor 2 (1 = forward / 2 = backwards)
try:
	j = pygame.joystick.Joystick(0) # create a joystick instance
	j.init() # init instance
	print 'Enabled joystick: ' + j.get_name()
except pygame.error:
	print 'no joystick found.'


while 1:
	for e in pygame.event.get(): # iterate over event stack
		if e.type == pygame.locals.JOYAXISMOTION: # Read Analog Joystick Axis
			x1 , y1 = j.get_axis(0), j.get_axis(1) # Left Stick
			y2 , x2 = j.get_axis(2), j.get_axis(3) # Right Stick

			print x1
			print y1
			print x2
			print y2

			if x1 < -1 * deadZone:
				 print 'Left Joystick 1'

			if x1 > deadZone:
				 print 'Right Joystick 1'

			if y1 <= deadZone and y1 >= -1 * deadZone:
	 m1 = 0 # Dont go forward or backwards

			if y1 < -1 * deadZone:
				 print 'Up Joystick 1'
				 m1 = 1 # go forward
				 print m1
				 
			if y1 > deadZone:
				 print 'Down Joystick 1'
				 m1 = 2 # go forward
				 print m1

			if y2 <= deadZone and y2 >= -1 * deadZone:
	 m2 = 0 # Dont go forward or backwards
				  
			if y2 < -1 * deadZone:
				 print 'Up Joystick 2'
				 m2 = 1

			if y2 > deadZone:
				 print 'Down Joystick 2'
				 m2 = 2

			if x2 < -1 * deadZone:
				print 'Left Joystick 2'

			if x2 > deadZone:
				print 'Right Joystick 2'

			
	if m1 == 1: # motor 1 go forward
# step 1 motor 1
		GPIO.output(8,GPIO.LOW)
		GPIO.output(16,GPIO.LOW)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)

	if m2 == 1: # motor 2 go forward
# step 1 motor 2
		GPIO.output(11,GPIO.LOW)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(15,GPIO.HIGH)
		GPIO.output(21,GPIO.HIGH)

	time.sleep(stepDelay)



	if m1 == 1: # motor 1 go forward
# step 2 motor 1
		GPIO.output(8,GPIO.HIGH)
		GPIO.output(16,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(22,GPIO.HIGH)

	if m2 == 1: # motor 2 go forward
# step 2 motor 2
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(21,GPIO.HIGH)

	time.sleep(stepDelay)

	if m1 == 1: # motor 1 go forward
# step 3 motor 1
		GPIO.output(8,GPIO.HIGH)
		GPIO.output(16,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(22,GPIO.LOW)

	if m2 == 1: # motor 2 go forward
# step 3 motor 2
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(21,GPIO.LOW)

	time.sleep(stepDelay)

	if m1 == 1: # motor 1 go forward
# step 4 motor 1
		GPIO.output(8,GPIO.LOW)
		GPIO.output(16,GPIO.HIGH)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(22,GPIO.LOW)

	if m2 == 1: # motor 2 go forward
# step 4 motor 2
		GPIO.output(11,GPIO.LOW)
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)
		GPIO.output(21,GPIO.LOW)

	time.sleep(stepDelay)

	if m1 == 2: # motor 1 go reverse
# step 4 motor 1
		GPIO.output(8,GPIO.LOW)
		GPIO.output(16,GPIO.HIGH)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(22,GPIO.LOW)

	if m2 == 2: # motor 2 go reverse
# step 4 motor 2
		GPIO.output(11,GPIO.LOW)
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)
		GPIO.output(21,GPIO.LOW)

	time.sleep(stepDelay)

	if m1 == 2: # motor 1 go reverse
# step 3 motor 1
		GPIO.output(8,GPIO.HIGH)
		GPIO.output(16,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(22,GPIO.LOW)

	if m2 == 2: # motor 2 go reverse
# step 3 motor 2
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(21,GPIO.LOW)

	time.sleep(stepDelay)

	if m1 == 2: # motor 1 go reverse
# step 2 motor 1
		GPIO.output(8,GPIO.HIGH)
		GPIO.output(16,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(22,GPIO.HIGH)

	if m2 == 2: # motor 2 go reverse
# step 2 motor 2
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(21,GPIO.HIGH)

	time.sleep(stepDelay)

	if m1 == 2: # motor 1 go reverse
# step 1 motor 1
		GPIO.output(8,GPIO.LOW)
		GPIO.output(16,GPIO.LOW)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)

	if m2 == 2: # motor 2 go reverse
# step 1 motor 2
		GPIO.output(11,GPIO.LOW)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(15,GPIO.HIGH)
		GPIO.output(21,GPIO.HIGH)

	time.sleep(stepDelay)
