import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'



GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT) 
GPIO.setup(19, GPIO.OUT) 
GPIO.setup(20, GPIO.OUT) 

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
    GPIO.output(19,False)
    GPIO.output(20,False)

    time.sleep(speed)
    
    GPIO.output(18,False)

    time.sleep(speed)
    GPIO.output(17,False)
    GPIO.output(18,True)

    time.sleep(speed)
    GPIO.output(17,True)
    GPIO.output(18,True)



def drawNumber(digit1,digit2,digit3,digit4):
    
    GPIO.output(17,False)
    GPIO.output(18,False)
    GPIO.output(19,False)
    GPIO.output(20,False)
    
    if digit1 == 1:
        GPIO.output(17,True)
        
    if digit2 == 1:
        GPIO.output(18,True)
        
    if digit3 == 1:
        GPIO.output(19,True)
        
    if digit4 == 1:
        GPIO.output(20,True)

    time.sleep(speed)

drawNumber(0,0,0,0) ## 6
drawNumber(1,0,0,0) ## nothing
drawNumber(1,1,0,0) ## 9
drawNumber(1,1,1,0) ##
drawNumber(1,1,1,1)
drawNumber(0,1,0,0)
drawNumber(0,1,1,1)
drawNumber(0,0,1,1)


    
    
 
        
