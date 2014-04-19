#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-24 16:02:08
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-26 19:21:17

from handlers.base import *
from model.base import Switch, User, Task
from error import HTTPAPIError
from scheduler.scheduler import *
import time
from datetime import datetime
import json

class TaskHandler(RestHandler):

	def get(self):
		data = self.get_request_data()
		page = data['page']
		page_size = 10;
		user_id = data['user_id']
		tasks = self.session.query(Task).filter(Task.user_id == user_id).offset((int(page)-1)*page_size).limit(page_size).all()
		tasks = {'tasks':[task.to_dict() for task in tasks]}
		self.finish(tasks)

	def post(self):
		data = self.get_request_data()
		switch_id = data['switch_id']

		if self.session.query(Switch).get(switch_id) is None :
			raise HTTPAPIError(404)

		user_id = self.get_argument('user_id')
		if self.session.query(User).get(user_id) is None :
			raise HTTPAPIError(404)

		target_status = self.get_argument('target_status')
		if_expression = self.get_argument('if_expression')
		create_time = datetime.now()
		modified_time = datetime.now()
		task = Task(switch_id = switch_id, user_id = user_id, target_status = target_status, if_expression = if_expression, create_time = create_time, modified_time = modified_time )
		self.session.add(task)
		self.session.commit()

		dict_exp = json.loads(if_expression)

		sched.add_interval_job(lambda:checkConditions(dict_exp,task.id),hours = 0.5)
		sched.start()

		result = {"result":"1"}
		self.finish(result)

	def put(self):
		data = self.get_request_data()
		task_id = data['task_id']
		result = data['result']
		task = self.session.query(Task).get(task_id)
		task.result = int(result)
		self.session.commit()
		task.notifyCallbacks()

class GetTaskResultHandler(BaseWebsockHandler):

	def open(self):
		Task.register(self.callback)

	def on_close(self):
		Task.unregister(self.callback)

	def on_message(self,msg):
		pass

	def callback(self,task_id,result):
		self.write_message('{"task_id":"%s","result":"%d"}'%(task_id,result))
