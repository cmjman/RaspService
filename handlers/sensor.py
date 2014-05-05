#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-03-24 18:47:27
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-25 15:29:25

from handlers.base import RestHandler
from model.base import Sensor,SensorData
from datetime import datetime
import pdb

class SensorHandler(RestHandler):
	def post(self):
		data = self.get_request_data()
		name = data['name']
		s_type = data['type']
		sensor = Sensor(sensor_name = name, sensor_type = s_type)

		self.session.add(sensor)
		self.session.commit()

class SensorDataHandler(RestHandler):
	def get(self,sensor_id):
		datas = self.session.query(SensorData).filter(SensorData.sensor_id == sensor_id).all()
		datas = {'sensorDatas':{'sensorDatas':[data.to_dict()['id'] for data in datas]},'sensorData':[data.to_dict() for data in datas ]}
		#for test
		self.set_header("Access-Control-Allow-Origin", "*")
		self.write(datas)
