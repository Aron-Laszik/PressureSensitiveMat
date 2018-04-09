#Author: Aron Laszik
#License: SeeLab?
#Using: Adafruit_Python_ADS1x15 public domain github

import time
#Import event handlers
import sys
#Import ADC's Module
import Adafruit_ADS1x15
#Import RPIO GPIO Module
import RPI.GPIO as GPIO
#Set up the boardd numbering system
GPIO.setmode(GPIO.BOARD)



#Set up the board's output ports 17,27,23,34
channel_list = [17,23,27,34]
GPIO.setup(channel_list,GPIO.OUT)
#Get rid of magic numbers, label the output ports
#by their orientation
FAR_LEFT = 24
MIDDLE_LEFT = 22
MIDDLE_RIGHT = 27
FAR_RIGHT = 34

#Make a 16 bit ADC instance
#the address is specific to the high voltage being on and
#the busnum on all RPI's is 1
adc = Adafruit_ADS1x15.ADS1115(address=0x49,busnum=1)

#set gain to 1 to utilize full 3.3V input
GAIN = 1

#have the ADC start reading in values
adc.start_adc(1,GAIN)

while True:
    try:
        #Switch high voltages between each output and read values
        GPIO.output(FAR_LEFT,GPIO.HIGH)
        GPIO.output([MIDDLE_LEFT,MIDDLE_RIGHT,FAR_RIGHT],GPIO.LOW)
        #Read upper voltage
        adc.start_adc(0,GAIN)
        upper_far_left = adc.get_last_result()
        #Read lower last voltage
        adc.start_adc(1,GAIN)
        lower_far_left = adc.get_last_result()


        #switch to middle left and read results
        GPIO.output(MIDDLE_LEFT,GPIO.HIGH)
        GPIO.output([FAR_LEFT,MIDDLE_RIGHT,FAR_RIGHT],GPIO.LOW)
        #Read upper voltage
        adc.start_adc(0,GAIN)
        upper_middle_left = adc.get_last_result()
        #Read lower last voltage
        adc.start_adc(1,GAIN)
        lower_middle_left = adc.get_last_result()

        #switch to middle right and read results
        GPIO.output(MIDDLE_MIDDLE,GPIO.HIGH)
        GPIO.output([FAR_LEFT,MIDDLE_LEFT,FAR_RIGHT],GPIO.LOW)
        #Read upper voltage
        adc.start_adc(0,GAIN)
        upper_middle_right = adc.get_last_result()
        #Read lower last voltage
        adc.start_adc(1,GAIN)
        lower_middle_right = adc.get_last_result()

        #switch to far right and read results
        GPIO.output(FAR_RIGHT,GPIO.HIGH)
        GPIO.output([FAR_LEFT,MIDDLE_RIGHT,MIDDLE_LEFT],GPIO.LOW)
        #Read upper voltage
        adc.start_adc(0,GAIN)
        upper_far_right = adc.get_last_result()
        #Read lower last voltage
        adc.start_adc(1,GAIN)
        lower_far_right = adc.get_last_result()

        #Print read values
        print(upper_far_left+"   "+upper_middle_left+"   "+upper_middle_right
              +"   "+upper_far_right)
        print(lower_far_left+"   "+lower_middle_left+"   "+lower_middle_right
              +"   "+lower_far_right)
        print()
        print()

        #sleep for half of a second
        time.sleep(0.5)

    #Handle a ^C exit
    except KeyboardInterrupt:
        adc.stop_adc()
        GPIO.cleanup()
        sys.exit(0)

