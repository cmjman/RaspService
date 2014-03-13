#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:46:18
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-13 14:15:13

from model.base import User
from handlers.base import BaseHandler
import hashlib

class RegisterHandler(BaseHandler):
	def post(self):
		nick = self.get_argument('nick')
		password = self.get_argument('password')
		password_md5 = hashlib.md5(password).hexdigest().upper()
		user = self.session.query(User).filter(User.nick == nick).first()

		if user is None:
			user = User(nick=nick, password = password_md5)
			self.session.add(user)
			self.session.commit()
			result = 1
		else:
			result = 0
			
		result = {"result":result}	
		self.finish(result)


class LoginHandler(BaseHandler):
	def post(self):
		nick = self.get_argument('nick')
		password = self.get_argument('password')
		password_md5 = hashlib.md5(password).hexdigest().upper()
		user = self.session.query(User).filter(User.nick == nick).first()
		password_real = user.password
		result = {"result":password_md5 == password_real}
		
		self.finish(result)