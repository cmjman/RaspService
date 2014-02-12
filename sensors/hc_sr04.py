#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-02-12 21:25:46
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-02-12 21:48:24

class HC_SR04():

	def __init__(self):
	 	GPIO.setmode(GPIO.BCM)
		GPIO_TRIGGER = 23
		GPIO_ECHO = 24
		print "Ultrasonic Measurement init"

		GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
		GPIO.setup(GPIO_ECHO,GPIO.IN)
		GPIO.output(GPIO_TRIGGER,False)
		time.sleep(0.5)

	def getOutput(self):
		GPIO.output(GPIO_TRIGGER,True)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER, False)
		start = time.time()
		while GPIO.input(GPIO_ECHO)==0:
		  	start = time.time()

		while GPIO.input(GPIO_ECHO)==1:
		  	stop = time.time()
		elapsed = stop-start
		distance = elapsed * 34000
		distance = distance / 2

		print "Distance : %.1f" % distance

		GPIO.cleanup()