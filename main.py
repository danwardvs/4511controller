import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import random


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

speed = input("Enter length of delay: ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
#Blink(int(iterations),float(speed))

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


def RandomDisplay(speed):
    i = 0
    while i < 100:
        drawNumber(random.random()*2,random.random()*2,random.random()*2,random.random()*2)
        
        i+=1
        
    


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





RandomDisplay(speed)



    
    
 
        
