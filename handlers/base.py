#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 14:19:06
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-25 19:07:19

import tornado.web
from model.base import *

class BaseHandler(tornado.web.RequestHandler):
	def initialize(self):
		self.session = DB_Session()

	def finish(self, chunk=None):
		if chunk is None :
			chunk = {"result":"True"}
		super(BaseHandler, self).finish()
	
	def on_finish(self):
		self.session.close()
