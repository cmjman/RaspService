#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-02-12 16:52:34
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-25 14:37:18

from RPi import GPIO
import time

PIN = 4

class DHT11():

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIN,GPIO.OUT)
		GPIO.output(PIN,GPIO.HIGH)
		time.sleep(0.025)
		GPIO.output(PIN,GPIO.LOW)
		time.sleep(0.02)
		GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	

	def bin2dec(string_num):
		return str(int(string_num, 2))

	def getData(self):
		data = []
		for i in range(0,500):
		   data.append(GPIO.input(4))
		bit_count = 0
		tmp = 0
		count = 0
		HumidityBit = ""
		TemperatureBit = ""
		crc = ""
		try:
			while data[count] == 1:
				tmp = 1
				count = count + 1

			for i in range(0, 32):
				bit_count = 0

				while data[count] == 0:
					tmp = 1
					count = count + 1

				while data[count] == 1:
					bit_count = bit_count + 1
					count = count + 1

				if bit_count > 3:
					if i>=0 and i<8:
						HumidityBit = HumidityBit + "1"
					if i>=16 and i<24:
						TemperatureBit = TemperatureBit + "1"
				else:
					if i>=0 and i<8:
						HumidityBit = HumidityBit + "0"
					if i>=16 and i<24:
						TemperatureBit = TemperatureBit + "0"

		except:
			print "ERR_RANGE"
			exit(0)

		try:
			for i in range(0, 8):
				bit_count = 0

				while data[count] == 0:
					tmp = 1
					count = count + 1

				while data[count] == 1:
					bit_count = bit_count + 1
					count = count + 1

				if bit_count > 3:
					crc = crc + "1"
				else:
					crc = crc + "0"
		except:
			print "ERR_RANGE"
			exit(0)

		Humidity = self.bin2dec(HumidityBit)
		Temperature = self.bin2dec(TemperatureBit)

		if int(Humidity) + int(Temperature) - int(self.bin2dec(crc)) == 0:
			print "Humidity:"+ Humidity +"%"
			print "Temperature:"+ Temperature +"C"
		else:
			print "ERR_CRC"

	def getTemperature(self):
		self.getData()
		return self.Temperature

	def getHumidity(self):
		self.getData()
		return self.Humidity