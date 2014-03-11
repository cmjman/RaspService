#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-03-24 21:02:42
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-26 19:28:57

from datetime import datetime
from apscheduler.scheduler import Scheduler
from sensors.dht11 import DHT11
from sensors.hc_sr04 import HC_SR04
from sensors.hc_sr501 import HC_SR501
from model.base import *
import apscheduler
import re

session = DB_Session()
dht11 = DHT11(4)
sched = Scheduler()

def err_listener(ev):
    err_logger = logging.getLogger('schedErrJob')
    if ev.exception:
        err_logger.exception('%s error.', str(ev.job))
    else:
        err_logger.info('%s miss', str(ev.job))

sched.add_listener(err_listener, apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED)

regExp = "(>=|<=|>|<|!=|==|=)"

def opCompare(op,par1,par2):
	if op == "<=":
		return par1 <= par2
	elif op == ">=":
		return par1 >= par2
	elif op == "<":
		return par1 < par2
	elif op == ">":
		return par1 > par2
	elif op == "!=":
		return par1 != par2
	elif op == "==" or op == "=":
		return par1 == par2


def checkTemperatue(temperature):
	op = str(re.match(regExp,temperature))
	parseTemp = temperature.lstrip(op)
	temp = dht11.getTemperature()
	return opCompare(op,temp,parseTemp)

def checkHumidity(humidity):
	op = str(re.match(regExp,humidity))
	parseHumi = humidity.lstrip(op)
	humi = dht11.getHumidity()
	return opCompare(op,humi,parseHumi)


def checkConditions(conditions,taskId):

	result = 1

	for key in conditions.keys():
		if key == "temperature":
			result = result & checkTemperatue(conditions[key])
		elif key == "humidity":
			result = result & checkHumidity(conditions[key])

	if result :
		task = session.query(Task).get(taskId)
		task.result = 1
		session.commit()
		task.notifyCallbacks()



