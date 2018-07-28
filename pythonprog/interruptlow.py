import RPi.GPIO as x
import time
from time import sleep

global pulse
pulse=0
x.setmode(x.BCM)
x.setwarnings(False)
x.cleanup()
x.setup(18,x.OUT)
x.setup(12,x.OUT)
x.setup(24,x.IN,pull_up_down=x.PUD_UP)

def blinkingled():
        x.output(12,x.HIGH)
        sleep(1)
        x.output(12,x.LOW)
        sleep(1)

def printcallback(channel):
        print(channel)
        global pulse
        pulse+=1
        print(pulse)
        print("water in liters:",pulse/42.0)

x.add_event_detect(24,x.FALLING,callback=printcallback)

try:
        while(1):
                blinkingled()
except:
        print("program close")
        x.cleanup()
