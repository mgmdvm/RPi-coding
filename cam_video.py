import picamera
from time import *
from subprocess import call

camera = picamera.PiCamera(resolution=(1280, 720), framerate=30)
camera.hflip = True
camera.vflip = True

camera.start_preview()
sleep(2)
camera.capture('newimage.jpg')
camera.stop_preview()


camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()


converter = ['MP4Box -add video.h264 newvideo.mp4']
call(converter, shell=True)
