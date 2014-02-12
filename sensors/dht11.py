#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-02-12 16:52:34
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-02-12 22:57:45

from RPi import GPIO
import time

PIN = 7

class DHT11():
    
    def __init__(self):
    	GPIO.setwarnings(False)
    	GPIO.setmode(GPIO.BOARD)
	
    def getOutput(self):
		GPIO.setup(PIN,GPIO.OUT)
		GPIO.output(PIN,GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(PIN,GPIO.HIGH)
		i = 1
		j = 0
		data = []
		
		GPIO.setup(PIN,GPIO.IN)
		while GPIO.input(PIN) == 1:
		    continue
		while GPIO.input(PIN) == 0:
		    continue
		while GPIO.input(PIN) == 1:
		    continue

		while j<40:
		    k = 0
		    while GPIO.input(PIN) == 0:
			continue
		
		    while GPIO.input(PIN) == 1:
			k+=1
	 		if k>100:
			    break
		    if k<3:
			data.append(0)
		    else:
			data.append(1)
		    j+=1
	       	print "Sensor is working"

		humidity_bit=data[0:8]
		humidity_point_bit=data[8:16]
		temperature_bit=data[16:24]
		temperature_point_bit=data[24:32]
		check_bit=data[32:40]

		humidity=0
		humidity_point=0
		temperature=0
		temperature_point=0
		check=0

		for i in range(8):
	    	    humidity+=humidity_bit[i]*2**(7-i)
	            humidity_point+=humidity_point_bit[i]*2**(7-i)
	            temperature+=temperature_bit[i]*2**(7-i)
	            temperature_point+=temperature_point_bit[i]*2**(7-i)
	            check+=check_bit[i]*2**(7-i)

		tmp=humidity+humidity_point+temperature+temperature_point
		if check==tmp:
	     	    print "temperature is ", temperature,"wet is ",humidity,"%"
		else:
	    	    print "something is wrong the humidity,humidity_point,temperature,temperature_point,check is",humidity,humidity_point,temperature,temperature_point,check
