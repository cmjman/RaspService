#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-24 16:02:08
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-26 19:21:17

from handlers.base import * 
from model.base import Switch, User, Task
from error import HTTPAPIError
from scheduler.scheduler import sched
import time

class AddTaskHandler(BaseHandler):
	
	def post(self):
		switch_id = self.get_argument('switch_id')

		if self.session.query(Switch).get(switch_id) is None :
			raise HTTPAPIError(404)
		
		user_id = self.get_argument('user_id')
		if self.session.query(User).get(user_id) is None :
			raise HTTPAPIError(404)

		target_status = self.get_argument('target_status')
		if_expression = self.get_argument('if_expression')
		create_time = time.time
		modified_time = time.time
		task = Task(switch_id = switch_id, user_id = user_id, target_status = target_status, if_expression = if_expression, create_time = create_time, modified_time = modified_time )
		self.session.add(task)
		self.session.commit()

		sched.add_job(checkConditions(if_expression,task.task_id),hours = 0.5)
		sched.start()

		result = {"result":"1"}	
		self.finish(result)

class GetTaskHandler(BaseHandler):

	def get(self):
		page = self.get_argument('page')
		page_size = 10;
		user_id = self.get_argument('user_id')
		tasks = self.session.query(Task).filter(Task.user_id == user_id).offset((int(page)-1)*page_size).limit(page_size).all()
		tasks = {'tasks':[task.to_dict() for task in tasks]} 
		self.finish(tasks)

class GetTaskResultHandler(BaseWebsockHandler):

	def open(self):
		Task.register(self.callback)

	def on_close(self):
		Task.unregister(self.callback)
			
	def on_message(self,msg):
		pass

	def callback(self,task_id,result):
		self.write_message('{"task_id":"%s","result":"%d"}'%(task_id,result))

class ChangeTaskResultHandler(BaseHandler):

	def post(self):
		task_id = self.get_argument('task_id')
		result = self.get_argument('result')
		task = self.session.query(Task).get(task_id)
		task.result = int(result)
		self.session.commit()
		task.notifyCallbacks()