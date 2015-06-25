import RPi.GPIO as GPIO
from time import sleep
from array import array
import random

GPIO.setmode(GPIO.BOARD)

def lightOnButtonPress(inputPin, outputPin):
	if GPIO.input(inputPin):
		GPIO.output(outputPin, GPIO.HIGH)
	else:
		GPIO.output(outputPin, GPIO.LOW)

def lightButton(color):
	GPIO.output(color, GPIO.HIGH)
	sleep(1)
	GPIO.output(color, GPIO.LOW)
	sleep(1)
	return


GPIO.setup(8, GPIO.IN) # red input
GPIO.setup(18, GPIO.OUT) # red output
GPIO.setup(10, GPIO.IN) # blue input
GPIO.setup(22, GPIO.OUT) # blue output
GPIO.setup(12, GPIO.IN) # green input
GPIO.setup(38, GPIO.OUT) # green output
GPIO.setup(16, GPIO.IN) # yellow input
GPIO.setup(40, GPIO.OUT) # yellow output

redBUTTON = 8
redLIGHT = 18
blueBUTTON = 10
blueLIGHT = 22
greenBUTTON = 12
greenLIGHT = 38
yellowBUTTON = 16
yellowLIGHT = 40

#while True:
#	lightOnButtonPress(redBUTTON, redLIGHT)
#	lightOnButtonPress(yellowBUTTON, yellowLIGHT)
#	lightOnButtonPress(greenBUTTON, greenLIGHT)
#	lightOnButtonPress(blueBUTTON, blueLIGHT)

def getSimon(levels):
		light = random.randint(1,4)
		levels.append(light)
		
		for i in range(len(levels)):
			if levels[i] == 1:
				lightButton(redLIGHT)
			elif levels[i] == 2:
				lightButton(yellowLIGHT)
			elif levels[i] == 3:
				lightButton(greenLIGHT)
			elif levels[i] == 4:
				lightButton(blueLIGHT)		

		return levels

def blink(pin):
	GPIO.output(pin, GPIO.HIGH)
	sleep(.7)
	GPIO.output(pin, GPIO.LOW)
	sleep(.7)

def passedLevel():
	GPIO.output(redLIGHT, GPIO.HIGH)
	GPIO.output(yellowLIGHT, GPIO.HIGH)
	GPIO.output(greenLIGHT, GPIO.HIGH)
	GPIO.output(blueLIGHT, GPIO.HIGH)
	sleep(.7)
	GPIO.output(redLIGHT, GPIO.LOW)
	GPIO.output(yellowLIGHT, GPIO.LOW)
	GPIO.output(greenLIGHT, GPIO.LOW)
	GPIO.output(blueLIGHT, GPIO.LOW)
	sleep(.7)


def failedLevel():
	GPIO.output(redLIGHT, GPIO.HIGH)
	sleep(.7)
	GPIO.output(blueLIGHT, GPIO.HIGH)
	sleep(.7)
	GPIO.output(greenLIGHT, GPIO.HIGH)
	sleep(.7)
	GPIO.output(yellowLIGHT, GPIO.HIGH)
	sleep(.7)
	GPIO.output(redLIGHT, GPIO.LOW)
	sleep(.7)
	GPIO.output(blueLIGHT, GPIO.LOW)
	sleep(.7)
	GPIO.output(greenLIGHT, GPIO.LOW)
	sleep(.7)
	GPIO.output(yellowLIGHT, GPIO.LOW)
	sleep(.7)	



def playSimon():
	levels = []
	currentLevel = 1
	gameover = False

	while gameover == False:
		levels = getSimon(levels)

		for i in range(len(levels)):
			buttonPressed = False
			while buttonPressed == False:
				if GPIO.input(redBUTTON):
					blink(redLIGHT)
					buttonPressed = True
					if levels[i] != 1:
						gameover = True
						return currentLevel
				elif GPIO.input(yellowBUTTON):
					blink(yellowLIGHT)
					buttonPressed = True
					if levels[i] != 2:
						gameover = True
						return currentLevel
				elif GPIO.input(greenBUTTON):
					blink(greenLIGHT)
					buttonPressed = True
					if levels[i] != 3:
						gameover = True
						return currentLevel
				elif GPIO.input(blueBUTTON):
					blink(blueLIGHT)
					buttonPressed = True
					if levels[i] != 4:
						gameover = True
						return currentLevel
		currentLevel += 1
		sleep(1)
		passedLevel()


def main():
	levelReached = playSimon()
	failedLevel()
	print("GAMEOVER. YOU MADE IT TO LEVEL {}.".format(levelReached))
	GPIO.cleanup()
	return


main()
