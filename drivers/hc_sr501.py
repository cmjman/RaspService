#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-02-15 15:10:43
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-02-15 15:16:22

from RPi import GPIO
import time

GPIO_PIR = 7

class HC_SR501():

	def __init__(self):
	 	GPIO.setmode(GPIO.BCM)
		GPIO.setup(GPIO_PIR,GPIO.IN)
		print "PIR Module init"

	def getOutput(self):
		Current_State  = 0
		Previous_State = 0
 
		try:
		 
			print "Waiting for PIR to settle ..."
			 
			while GPIO.input(GPIO_PIR)==1:
				Current_State  = 0
			 
			print "  Ready"
			 
			while True :
			 
			    Current_State = GPIO.input(GPIO_PIR)
			 
			    if Current_State==1 and Previous_State==0:
			  		print "Motion detected!"
			  		Previous_State = 1
			    elif Current_State==0 and Previous_State==1:
			     	print "Ready"
			      	Previous_State=0

			    time.sleep(0.01)
			 
		except KeyboardInterrupt:
			print "  Quit"
			GPIO.cleanup()