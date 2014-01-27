#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-27 15:11:13
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-27 22:58:34


import sys
sys.path.append('..') #导入上级目录到搜索路径
from daemon.time_task import TimeTask

if __name__ == '__main__':
 	daemon = TimeTask('/tmp/pidfile',stdout='/tmp/result')
 	daemon.start_daemon()
