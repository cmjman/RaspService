#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 15:52:48
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-25 19:10:03

from handlers.base import BaseHandler 
from model.base import Switch
from error import HTTPAPIError

class AddSwitchHandler(BaseHandler):
	
	def post(self):
		name = self.get_argument('name')
		level = self.get_argument('level')
		switch = Switch(name = name, level = level)
		self.session.add(switch)
		self.session.commit()

class DelSwitchHandler(BaseHandler):

	def post(self):
		switch_id = self.get_argument('switch_id')
		switch = self.session.query(Switch).get(switch_id)
		if switch is None:
			raise HTTPAPIError(404)
		self.session.delete(switch)
		self.session.commit()