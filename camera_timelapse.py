# import modules needed or anticipated
import picamera
from time import *
from subprocess import call

# set camera variables
camera = picamera.PiCamera(resolution=(1280, 720), framerate=30)
camera.hflip = True
camera.vflip = True

#set time lapse variables by request to user
timeLapseNumber = input("How many pictures do you want?")
timeLapseFreq = input("How often do you want the pictures taken (in seconds)?")

# take pictures
for i in range(int(timeLapseNumber)):
    camera.capture('/home/pi/Desktop/timelapse/image{0:04d}.jpg'.format(i))
    print("Taking a picture now")
    sleep(int(timeLapseFreq))
    
                   
