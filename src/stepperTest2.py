import sys
import time
import RPi.GPIO as GPIO

def move(direction, distance, motor):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    if (motor == "bottom"):
        StepPins = [3,5,7,11]
    else:
        StepPins = [31,33,35,37]
    
    for pin in StepPins:
        print("pin setup of " + str(pin))
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)

    Seq = [[1,0,0,1],
           [1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,0,1,0],
           [0,0,1,1],
           [0,0,0,1]]   
    StepCount = len(Seq)
 
    # Initialise variables
    StepCounter = 0
    StepDir = direction
    duration = distance
 
    # Start main loop
    for x in range(1,duration):
 
      for pin in range(0,4):
        xpin=StepPins[pin]# Get GPIO
        if Seq[StepCounter][pin]!=0:
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
 
      StepCounter += StepDir
 
      # If we reach the end of the sequence
      # start again
      if (StepCounter>=StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount+StepDir
 
      # Wait before moving on
      time.sleep(.003)

    # Initialise variables
    StepDir = -2 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
    StepCounter = 0

