import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ControlPin = [17,18,21,22]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

rev = input("Enter the number of revolutions you want: ")
#dir = input("Enter the direction (1 CW / -1 CCW)")
cycle = int(rev) * 128
if cycle <20: cycle = 128
#dir = int(dir)
#if dir != 1 and dir != -1: dir = 1
#print(rev, dir)


for i in range(cycle):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep][pin])
            #Control_Pin = ControlPin[pin]
            #if seq[halfstep] [pin] == 1:
            #    GPIO.output(Control_Pin, True)
            #else:
            #    GPIO.output(Control_Pin, False)
                

            #halfstep += dir
            #if (halfstep >= 8):
            #    halfstep = 0
            #elif (halfstep < 0):
            #    halfstep = 7
                       
            time.sleep(0.001)

GPIO.cleanup()
print('Done')

