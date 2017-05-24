import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys


import Adafruit_MPR121.MPR121 as MPR121

#Setup
nButtons = 9
#Map buttons to pin numbers {button: pinNim}
buttonPins = {0:0, 1: 10, 2: 9, 3: 11, 4: 7, 5: 6, 6: 8, 7: 4, 8: 3, 9: 5, 10:1, 11:2}

print('Capacitive KeyPad Demo')

#Create MPR121 instance
cap = MPR121.MPR121()

#Init communication with MPR121 using default I2C bus
if not cap.begin():
    print('Error initialising MPR121')
    sys.exit(1)

print('Press ctrl-C to quit')
last_touched = cap.touched()

#Main loop
while True:
    current_touched = cap.touched()

    #Check each button
    for iBtn in buttonPins:
        pin_bit = 1 << buttonPins[iBtn]

        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            if iBtn == 10:
                print('* touched!')
            elif iBtn == 11:
                print('# touched!')
            else:
                print('{0} touched!'.format(iBtn))
            
        # Next check if transitioned from touched to not touched.
        if not current_touched & pin_bit and last_touched & pin_bit:
            if iBtn == 10:
                print('* released!')
            elif iBtn == 11:
                print('# released!')
            else:
                print('{0} released!'.format(iBtn))
        

    last_touched = current_touched
    time.sleep(0.1)
        
