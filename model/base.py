#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 14:24:19
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-16 18:44:52

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql.expression import text

#DB_CONNECT_STRING = "mysql+mysqldb://root:123456@192.168.1.150/rasp?charset=utf8"
DB_CONNECT_STRING = "mysql+mysqldb://root:123456@127.0.0.1/rasp?charset=utf8"
engine = create_engine(DB_CONNECT_STRING , echo = True)
DB_Session = sessionmaker(bind = engine)
session = DB_Session()

BaseModel = declarative_base()

def sqlalchemy_json(self):
    obj_dict = self.__dict__
    return dict((key, obj_dict[key]) for key in obj_dict if not key.startswith('_') and key.find('password'))
BaseModel.to_dict = sqlalchemy_json

def init_db():
	BaseModel.metadata.create_all(engine)

def drop_db():
	BaseModel.metadata.drop_all(engine)

class User(BaseModel):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True) 
	nick = Column(String(30))
	password = Column(String(32))   	#存储md5值
	picture = Column(String(30))  		#用户头像（预留）
	level = Column(Integer)       		#用户权限级别

class Switch(BaseModel):
	__tablename__ = 'switch'      

	id = Column(Integer, primary_key = True)
	name = Column(String(30))
	status = Column(Boolean, server_default = text('False'))      	#开关当前状态
	level = Column(Integer)       									#最小可操作等级

	callbacks = []
	@classmethod
	def register(cls, callback):
		cls.callbacks.append(callback)

	@classmethod
	def unregister(cls, callback):
		cls.callbacks.remove(callback)

	def notifyCallbacks(self):
		for callback in self.callbacks:
			callback(self.id,self.status)

class Task(BaseModel):
	__tablename__ = 'task'											#开关操作任务表，设置任务后由异步线程调用

	id = Column(Integer, primary_key = True)
	switch_id = Column(Integer)   
	user_id = Column(Integer)			
	target_status = Column(Boolean)									#目标状态 
	if_expression = Column(String(100))								#操作条件表达式，为空立即进行操作
	result = Column(Integer, server_default = text('0'))			#操作结果 0操作中，1成功，2失败
	create_time = Column(TIMESTAMP)    
	modified_time = Column(TIMESTAMP)

if __name__ == "__main__":
	#init_db()
	#drop_db()
	pass