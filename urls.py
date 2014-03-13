#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:41:30
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-13 14:15:58

from handlers.switch import *
from handlers.user import *
from handlers.task import *
from handlers.home import *

urls = [
('/service/addTask',AddTaskHandler),
('/service/getTask',GetTaskHandler),
('/service/addSwitch',AddSwitchHandler),
('/service/getSwitch',GetSwitchHandler),
('/service/delSwitch',DelSwitchHandler),
('/service/login',LoginHandler),
('/service/register',RegisterHandler),
('/',HomeHandler)
]