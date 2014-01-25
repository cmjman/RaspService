#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-20 10:46:18
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-25 10:17:10

from model.base import User
from handlers.base import BaseHandler
import hashlib

class RegisterHandler(BaseHandler):
	def post(self):
		nick = self.get_argument('nick')
		password = self.get_argument('password')
		password_md5 = hashlib.md5(password).hexdigest().upper()
		user = User(nick=nick, password = password_md5)
		self.session.add(user)
		self.session.commit()

class LoginHandler(BaseHandler):
	def post(self):
		user_id = self.get_argument('user_id')
		password = self.get_argument('password')
		password_md5 = hashlib.md5(password).hexdigest().upper()
		password_real = self.session.query(User).get(user_id).password
		result = {"result":password_md5 == password_real}
		
		self.write(result)