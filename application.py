#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:39:14
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-23 16:22:02

from urls import urls

import tornado.web

application = tornado.web.Application(handlers = urls)