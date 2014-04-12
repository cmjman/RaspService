#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-03-24 18:47:27
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-25 15:29:25

from handlers.base import BaseHandler
from model.base import Sensor,SensorData
from datetime import datetime

class AddSensorHandler(BaseHandler):
	def post(self):
		name = self.get_argument('name')
		s_type = self.get_argument('type')
		sensor = Sensor(sensor_name = name, sensor_type = s_type)

		self.session.add(sensor)
		self.session.commit()

class GetSensorDataHandler(BaseHandler):
	def get(self):
		sensor_id = self.get_argument('sensor_id')
		sensor_data = self.session.query(SensorData).filter(SensorData.sensor_id == sensor_id).limit(1).all()
		self.finish(sensor_data.to_dict())