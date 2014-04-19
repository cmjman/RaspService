#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:46:18
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-15 22:11:50

from model.base import User
from handlers.base import RestHandler
import hashlib


class UserHandler(RestHandler):

	def get(self):
		data = self.get_request_data()
		nick = data['nick']
		password = data['password']
		password_md5 = hashlib.md5(password).hexdigest().upper()
		user = self.session.query(User).filter(User.nick == nick).first()
		password_real = user.password
		if password_md5 == password_real:
			result = {"result":"1","user":user.to_dict()}
		else:
			result = {"result":"0"}

		self.finish(result)

	def post(self):
		data = self.get_request_data()
		nick = data['nick']
		password = data['password']
		password_md5 = hashlib.md5(password).hexdigest().upper()
		user = self.session.query(User).filter(User.nick == nick).first()

		if user is None:
			user = User(nick=nick, password = password_md5, picture = '',level = '')
			self.session.add(user)
			self.session.commit()
			result = 1
		else:
			result = 0

		result = {"result":result}
		self.finish(result)
