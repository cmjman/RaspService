#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 16:41:14
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-30 18:53:28

import urllib
import urllib2
import unittest
import json

HOST_URL = "http://127.0.0.1:8080/service/"
REMOTE_URL ="http://192.168.1.111:8080/service/"

class HttpTestCase(unittest.TestCase):

	def post(self,url, data):
		req = urllib2.Request(url)
		data = urllib.urlencode(data)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(req, data)
		return response.read()

	def get(self,url, data):
		data = urllib.urlencode(data)
		full_url = url + '?' + data
		response = urllib.urlopen(full_url)
		return str(response.info())+response.read()

	def registerTest():
		posturl = HOST_URL + "register"
		data = {'nick':'testUser','password':'123456'}
		print post(posturl, data)

	def loginTest():
		posturl = "http://127.0.0.1:8080/service/login"
		data = {'user_id':'1','nick':'testUser','password':'123456'}
		print post(posturl, data)

	def _test_addTask(self):
		user_id =1
		switch_id = 1
		posturl =  REMOTE_URL + "addTask"

		#if_expression = {"temperature":"20-30","humidity":"12,17"}
		if_expression = {"temperature":">20"}
		exp_json = json.dumps(if_expression)
		data = {'user_id':user_id,'switch_id':switch_id,'target_status':'1','if_expression':exp_json}
		print self.post(posturl, data)

	def _test_addSensor(self):
		name = "dht11"
		s_type = 1
		posturl = REMOTE_URL + "addSensor"
		data = {'name':name,'type':type}
		print self.post(posturl,data)

	def _test_addSwitch(self):
		name ="test"
		level = 0
		posturl = REMOTE_URL+"addSwitch"
		data = {'name':name,'level':level}
		print self.post(posturl, data)

	def delSwitchTest():
		posturl = HOST_URL+ "delSwitch"
		data = {'switch_id':'2'}
		print post(posturl, data)

	def _test_getSwitch(self):
		page = 1
		url = REMOTE_URL + "getSwitch"
		data = {'page':page}
		print self.get(url, data)

	def etag_get(self,url, data):
		data = urllib.urlencode(data)
		full_url = url + '?' + data
		req = urllib2.Request(full_url)
		#使用'8f475faacbd75cbfdc746d6ca10813e7230cd4cc'会报200，格式不同
		req.add_header('If-None-Match','"8f475faacbd75cbfdc746d6ca10813e7230cd4cc"')
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(req)
		return str(response.info())+response.read()

	def test_etag_getSwitch(self):
		page = 1
		url = REMOTE_URL + "getSwitch"
		data = {'page':page}
		print self.etag_get(url, data)

	def changeSwitchStatusTest(switch_id,status):
		posturl = "http://127.0.0.1:8080/service/changeSwitchStatus"
		data = {'switch_id':switch_id,'status':status}
		print post(posturl, data)

if __name__ == '__main__':
	unittest.main()
	#registerTest()
	#loginTest()
	#addTaskTest()
	#delSwitchTest()
	#for integer in range(10):
		#addSwitchTest("switch"+str(integer),"0")
	#etSwitchTest(1)
	#for integer in range(10):
		#addTaskTest("1",str(integer+1))
	#changeSwitchStatusTest("3","1");

	pass
