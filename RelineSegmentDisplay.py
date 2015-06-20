import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT) # top left
GPIO.setup(22, GPIO.OUT) # middle
GPIO.setup(38, GPIO.OUT) # bottom left
GPIO.setup(40, GPIO.OUT) # bottom
GPIO.setup(26, GPIO.OUT) # top
GPIO.setup(32, GPIO.OUT) # top right
GPIO.setup(36, GPIO.OUT) # bottom right

GPIO.setup(8, GPIO.IN) # bit1
GPIO.setup(10, GPIO.IN) # bit2
GPIO.setup(12, GPIO.IN) # bit3
GPIO.setup(16, GPIO.IN) # bit4

bit1 = 0
bit2 = 0
bit3 = 0
bit4 = 0

def buttonCheck():
	global bit1
	global bit2
	global bit3
	global bit4

	if GPIO.input(8):
		if bit1 == 0:
			bit1 = 1
		elif bit1 == 1:
			bit1 = 0
	if GPIO.input(10):
		if bit2 == 0:
			bit2 = 1
		elif bit2 == 1:
			bit2 = 0
	if GPIO.input(12):
		if bit3 == 0:
			bit3 = 1
		elif bit3 == 1:
			bit3 = 0
	if GPIO.input(16):
		if bit4 == 0:
			bit4 = 1
		elif bit4 == 1:
			bit4 = 0
	
def determineHEX():
	hex = bit1 + bit2*2 + bit3*4 + bit4*8
	if hex == 10:
		return 'A'
	elif hex == 11:
		return 'b'
	elif hex == 12:
		return 'C'
	elif hex == 13:
		return 'd'
	elif hex == 14:
		return 'E'
	elif hex == 15:
		return 'F'
	else:
		return hex

def displayHEX(hex):
	if hex == 0:			
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)

	if hex == 1:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(40, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)

	if hex == 2:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.LOW)
		
	if hex == 3:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 4:
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(40, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 5:
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.LOW)
		GPIO.output(36, GPIO.HIGH)
		
	
	if hex == 6:
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.LOW)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 7:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(40, GPIO.LOW)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 8:
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 9:
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 'A':
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.LOW)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 'b':
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(32, GPIO.LOW)
		GPIO.output(36, GPIO.HIGH)
		

	if hex == 'C':
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.LOW)
		GPIO.output(36, GPIO.LOW)
		

	if hex == 'd':
		GPIO.output(18, GPIO.LOW)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(32, GPIO.HIGH)
		GPIO.output(36, GPIO.HIGH)
		
	if hex == 'E':
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.LOW)
		GPIO.output(36, GPIO.LOW)
		

	if hex == 'F':
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.LOW)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(32, GPIO.LOW)
		GPIO.output(36, GPIO.LOW)
		

while True:
	buttonCheck()
	displayHEX(determineHEX())
	



#GPIO.output(18, GPIO.HIGH)
#GPIO.output(22, GPIO.HIGH)
#sleep(1)
#GPIO.output(22, GPIO.LOW)
#GPIO.output(38, GPIO.HIGH)
#sleep(1)
#GPIO.output(38, GPIO.LOW)
#GPIO.output(40, GPIO.HIGH)
#sleep(1)
#GPIO.output(40, GPIO.LOW)
#GPIO.output(26, GPIO.HIGH)
#sleep(1)
#GPIO.output(26, GPIO.LOW)
#GPIO.output(32, GPIO.HIGH)
#sleep(1)
#GPIO.output(32, GPIO.LOW)
#GPIO.output(36, GPIO.HIGH)
#sleep(1)
#GPIO.output(36, GPIO.LOW)
#GPIO.output(18, GPIO.LOW)


GPIO.cleanup()
