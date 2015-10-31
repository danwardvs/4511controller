import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'



GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT) 


##Define a function named Blink()
def Blink(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes
        ## ## print( "Iteration " + str(i+1))## Print current loop
        GPIO.output(17,True)## Switch on pin 7
        time.sleep(speed)## Wait
        GPIO.output(17,False)## Switch off pin 7
        time.sleep(speed)## Wait
    print ("Done") ## When loop is complete, print "Done"
    GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
#iterations = input("Enter total number of times to blink: ")
speed = input("Enter length of each blink(seconds): ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
#Blink(int(iterations),float(speed))


def Scroll(speed):
    
    GPIO.output(17,False)
    GPIO.output(18,False)

    time.sleep(speed)
    GPIO.output(17,True)
    GPIO.output(18,False)

    time.sleep(speed)
    GPIO.output(17,False)
    GPIO.output(18,True)

    time.sleep(speed)
    GPIO.output(17,True)
    GPIO.output(18,True)
    
Scroll(speed)    
        
