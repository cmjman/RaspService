#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-02-12 16:52:34
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-30 19:59:57
import sys
sys.path.append('..')
from sensors.dht11 import DHT11
from sensors.hc_sr04 import HC_SR04
from sensors.hc_sr501 import HC_SR501

import time
import unittest

class SensorTestCase(unittest.TestCase):

	def test_dht11(self):
		dht11 = DHT11(4)   
		print dht11.getTemperature()
		print dht11.getHumidity()

	def _test_time(self):
		
		a=time.time()
		i=1
		c=time.time()
		d=c-a
		print d

		a=time.time()
		for i in range(100):
			j+=1
		c=time.time()
		d=c-a
		print d

if __name__ == '__main__':

	unittest.main()
  
	#hc_sr04 = HC_SR04()
	#hc_sr04.getOutput()
	#hc_sr501 = HC_SR501()
	#hc_sr501.getOutput()
