#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 14:19:06
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-13 13:35:47

import tornado.web
from model.base import *

class BaseHandler(tornado.web.RequestHandler):
	def initialize(self):
		self.session = DB_Session()

	def finish(self, chunk=None):
		if chunk is None :
			chunk = {}

		if isinstance(chunk, dict):
			chunk = {"meta":{"code":200}, "response": chunk}

		self.set_header("Content-Type","application/json; charset=UTF-8")
		super(BaseHandler, self).finish(chunk)
	
	def on_finish(self):
		self.session.close()
