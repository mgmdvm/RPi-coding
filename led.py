import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



GPIO.setup(19,GPIO.OUT)
print ("LED on")
GPIO.output(19,GPIO.HIGH)
time.sleep(3)
print ("LED off")
GPIO.output(19,GPIO.LOW)

GPIO.setup(6,GPIO.OUT)
print ("LED on")
GPIO.output(6,GPIO.HIGH)
time.sleep(3)
print ("LED off")
GPIO.output(6,GPIO.LOW)

GPIO.setup(21,GPIO.OUT)
print ("LED on")
GPIO.output(21,GPIO.HIGH)
time.sleep(3)
print ("LED off")
GPIO.output(21,GPIO.LOW)
time.sleep(1)

led = (6, 19, 21)
x = 0
while x < 5:
    GPIO.setup(led,GPIO.OUT)
    print ("LED on")
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(led,GPIO.LOW)
    time.sleep(0.5)
    x += 1

GPIO.setup(led, GPIO.OUT)

p = GPIO.PWM(19,50)
p1 = GPIO.PWM(6,50)
p2 = GPIO.PWM(21,50)
p.start(0)
p1.start(0)
p2.start(0)

for j in range(5):
#try:
        #while True:
            for i in range(100):
                p.ChangeDutyCycle(i)
                p1.ChangeDutyCycle(i)
                p2.ChangeDutyCycle(i)
                time.sleep(0.02)
                
            for i in range(100):
                p.ChangeDutyCycle(100-i)
                p1.ChangeDutyCycle(100-i)
                p2.ChangeDutyCycle(100-i)
                time.sleep(0.02)
                
                
#except KeyboardInterrupt:
p.stop()
p1.stop()
p2.stop()
GPIO.cleanup()
