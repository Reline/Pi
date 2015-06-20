__author__ = 'Nathan'

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)

# GPIO.output(11, GPIO.LOW)
# sleep(1)
# GPIO.output(11, GPIO.HIGH)

def fibonacci(counter):
    prevNumber = 0
    currentNumber = 1
    loop = 0

    while loop != counter:
        # flash currentNumber of times
        currentNumber += prevNumber
        prevNumber = currentNumber - prevNumber
        loop += 1

    return 0
