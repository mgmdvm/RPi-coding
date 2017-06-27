#import needed libraries
import time
import RPi.GPIO as GPIO

#set GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Output pins for this motor (more motors to be added)
axisx = [17,18,21,22]

#setting pin state to low to start
for pin in axisx:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

#Array for pin states to halfstep motor
seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

#Get user input for number of steps and direction via negative or positive number
stepsx = input("How many X steps forward or backward (neg numbers reverse directions)? ")

#look at while loop to run more than once if requested, need input of Y/N
# at end to cause loop back to this point While true? maybe Y= True, N= False
#negative number runs first in a CCW direction
if int(stepsx) < 0:
    seq.reverse()
    for i in range(-int(stepsx)):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(axisx[pin], seq[halfstep][pin])
            time.sleep(0.001)
    seq.reverse()

#if the number is positive then this runs in a CW direction
else:
     for i in range(int(stepsx)):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(axisx[pin], seq[halfstep][pin])
            time.sleep(0.001)


#clean up pins after complete and give indication process finished
GPIO.cleanup()
print('Done')

