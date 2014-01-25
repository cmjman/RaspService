#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:41:30
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-25 17:06:47

from handlers.switch import *
from handlers.user import *
from handlers.task import *

urls = [
('/service/addTask',AddTaskHandler),
('/service/addSwitch',AddSwitchHandler),
('/service/delSwitch',DelSwitchHandler),
('/service/login',LoginHandler),
('/service/register',RegisterHandler)
]