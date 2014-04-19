#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:17:17
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-20 10:38:17

import tornado.ioloop
import sys

from route import application

PORT = '8080'
IP = '0.0.0.0'

if __name__ == "__main__":
	if len(sys.argv) > 1:
		PORT = sys.argv[1]
	#for RaspPi
	#http://stackoverflow.com/questions/16153804/tornado-socket-error-on-arm
	application.listen(PORT,IP)
	print 'Server is running at http://127.0.0.1:%s/' % PORT
	print 'Quit the server with CONTROL-C'
	tornado.ioloop.IOLoop.instance().start()
