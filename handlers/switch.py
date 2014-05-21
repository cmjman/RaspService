#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 15:52:48
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-16 18:47:28

from handlers.base import *
from model.base import Switch
from error import HTTPAPIError
from drivers import LED

class SwitchHandler(RestHandler):

	def get(self):
		data = self.get_request_data()
		page = data['page']
		page_size = 10;
		switches = self.session.query(Switch).offset((int(page)-1)*page_size).limit(page_size).all()
		switches = {'switches':[switch.to_dict() for switch in switches]}
		self.finish(switches)

	def post(self):
		data = self.get_request_data()
		name = data['name']
		level = data['level']
		picture = data['picture']
		switch = Switch(name = name, level = level, picture = picture)
		self.session.add(switch)
		self.session.commit()

	def put(self):
		data = self.get_request_data()
		switch_id = data['switch_id']
		status = data['status']
		switch = self.session.query(Switch).get(switch_id)
		switch.status = int(status)
		self.session.commit()
		l = LED()
		l.turn(switch.status)
		switch.notifyCallbacks()

	def delete(self):
		data = self.get_request_data()
		switch_id = data['switch_id']
		switch = self.session.query(Switch).get(switch_id)
		if switch is None:
			raise HTTPAPIError(404)
		self.session.delete(switch)
		self.session.commit()

class GetSwitchStatusHandler(BaseWebsockHandler):

	def open(self):
		Switch.register(self.callback)

	def on_close(self):
		Switch.unregister(self.callback)

	def on_message(self,msg):
		pass

	def callback(self,switch_id,status):
		self.write_message('{"switch_id":"%s","status":"%d"}'%(switch_id,status))
