from RPi import GPIO
from time import sleep
import time
import sys
import Adafruit_MPR121.MPR121 as MPR121

#Setup
nButtons = 9
#Map buttons to pin numbers {button: pinNim}
buttonPins = {0:0, 1: 10, 2: 9, 3: 11, 4: 7, 5: 6, 6: 8, 7: 4, 8: 3, 9: 5, 10:1, 11:2}

#Create MPR121 instance
cap = MPR121.MPR121()

#Init communication with MPR121 using default I2C bus
if not cap.begin():
    print('Error initialising MPR121')
    sys.exit(1)
	
last_touched = cap.touched()


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Setup outputs for LEDs
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

try:
    while True:
        		
	current_touched = cap.touched()

        #Check each button
        for iBtn in buttonPins:
            pin_bit = 1 << buttonPins[iBtn]

            # First check if transitioned from not touched to touched.
            if current_touched & pin_bit and not last_touched & pin_bit:
		if iBtn == 1:
		    GPIO.output(8, True)
		if iBtn == 2:
		    GPIO.output(12, True)
		if iBtn == 3:
		    GPIO.output(16, True)
		if iBtn == 4:
		    GPIO.output(22, True)
		if iBtn == 5:
		    GPIO.output(26, True)
            if not current_touched & pin_bit and last_touched & pin_bit:
		if iBtn == 1:
		    GPIO.output(8, False)
		if iBtn == 2:
		    GPIO.output(12, False)
		if iBtn == 3:
		    GPIO.output(16, False)
		if iBtn == 4:
		    GPIO.output(22, False)
		if iBtn == 5:
		    GPIO.output(26, False)
            
        

        last_touched = current_touched
        time.sleep(0.1)
	
except KeyboardInterrupt:
    GPIO.output(8, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(22, False)
    GPIO.output(26, False)
  

