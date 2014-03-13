#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-24 16:02:08
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-13 14:17:24

from handlers.base import BaseHandler 
from model.base import Switch, User, Task
from error import HTTPAPIError
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

class GetTaskHandler(BaseHandler):

	def get(self):
		page = self.get_argument('page')
		page_size = 10;
		tasks = self.session.query(Task).offset((int(page)-1)*page_size).limit(page_size).all()
		tasks = {'tasks':[task.to_dict() for task in tasks]} 
		self.finish(tasks)