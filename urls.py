#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:41:30
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-16 00:15:32

from handlers.switch import *
from handlers.user import *
from handlers.task import *
from handlers.home import *
from handlers.sensor import *

base = '/service/'

urls = [
(base+'addTask',AddTaskHandler),
(base+'getTask',GetTaskHandler),
(base+'addSwitch',AddSwitchHandler),
(base+'getSwitch',GetSwitchHandler),
(base+'getSwitchStatus',GetSwitchStatusHandler),
(base+'changeSwitchStatus',ChangeSwitchStatusHandler),
(base+'delSwitch',DelSwitchHandler),
(base+'addSensor',AddSesnorHandler),
(base+'login',LoginHandler),
(base+'register',RegisterHandler),
('/',HomeHandler)
]
