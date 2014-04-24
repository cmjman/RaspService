#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 14:19:06
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-16 00:09:08

from tornado_rest_handler import TornadoRestHandler
import tornado.websocket
from model.base import *

class RestHandler(TornadoRestHandler):
	def initialize(self):
		self.session = DB_Session()

	def on_finish(self):
		self.session.close()

class BaseWebsockHandler(tornado.websocket.WebSocketHandler):
	def initialize(self):
		self.session = DB_Session()
