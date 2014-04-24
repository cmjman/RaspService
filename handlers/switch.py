#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 15:52:48
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-16 18:47:28

from handlers.base import *
from model.base import Switch
from error import HTTPAPIError


class SwitchHandler(RestHandler):

	def get(self):
		page = self.get_argument('page')
		page_size = 10;
		switches = self.session.query(Switch).offset((int(page)-1)*page_size).limit(page_size).all()
		switches = {'switches':[switch.to_dict() for switch in switches]}
		self.finish(switches)

	def post(self):
		name = self.get_argument('name')
		level = self.get_argument('level')
		picture = self.get_argument('picture')
		switch = Switch(name = name, level = level, picture = picture)
		self.session.add(switch)
		self.session.commit()

	def put(self):
		switch_id = self.get_argument('switch_id')
		status = self.get_argument('status')
		switch = self.session.query(Switch).get(switch_id)
		switch.status = int(status)
		self.session.commit()
		switch.notifyCallbacks()

	def delete(self):
		switch_id = self.get_argument('switch_id')
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
