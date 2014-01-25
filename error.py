#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-25 16:40:33
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-25 16:49:52

from tornado import escape
from tornado.web import HTTPError

class HTTPAPIError(HTTPError):
	
	def __str__(self):
		err={"result":"False"}
		return escape.json_encode(err)
