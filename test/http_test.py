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
REMOTE_URL ="http://192.168.1.112:8080/service/"

class HttpTestCase(unittest.TestCase):

	def get(self,url, data):
		data = urllib.urlencode(data)
		full_url = url + '?' + data
		response = urllib.urlopen(full_url)
		return str(response.info())+response.read()

	def post(self,url, data):
		req = urllib2.Request(url)
		data = urllib.urlencode(data)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(req, data)
		return response.read()

	def put(self,url,data):
		req = urllib2.Request(url)
		req.get_method = lambda:"PUT"
		data = urllib.urlencode(data)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(req, data)
		return response.read()

	def delete(self,url,data):
		req = urllib2.Request(url)
		req.get_method = lambda:"DELETE"
		data = urllib.urlencode(data)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(req, data)
		return response.read()

	def _test_user_post(self):
		posturl = REMOTE_URL + "user"
		data = {'nick':'testUser','password':'123456'}
		print self.post(posturl, data)

	def _test_user_get(self):

		user_id = 1
		password = '123456'
		url =  REMOTE_URL + "user"
		data = {'user_id':user_id,'password':password}

		print self.get(url,data)

	def _test_task_post(self):
		user_id =1
		switch_id = 1
		posturl =  REMOTE_URL + "task"

		#if_expression = {"temperature":"20-30","humidity":"12,17"}
		if_expression = {"temperature":">20"}
		exp_json = json.dumps(if_expression)
		data = {'user_id':user_id,'switch_id':switch_id,'target_status':'1','if_expression':exp_json}
		print self.post(posturl, data)

	def test_task_get(self):
		page = 1
		user_id = 1
		url =  REMOTE_URL + "task"
		data = {'user_id':user_id,'page':page}
		print self.get(url,data)

	def test_sensor_post(self):
		name = "dht11"
		s_type = 1
		posturl = REMOTE_URL + "sensor"
		data = {'name':name,'type':type}
		print self.post(posturl,data)

	def test_switch_post(self):
		name ="test"
		level = 0
		picture = "picture"
		posturl = REMOTE_URL+"switch"
		data = {'name':name,'level':level,'picture':picture}
		print self.post(posturl, data)

	def test_switch_delete(self):
		posturl = REMOTE_URL+ "switch"
		data = {'switch_id':'1'}
		print self.delete(posturl, data)

	def _test_switch_get(self):
		page = 1
		url = REMOTE_URL + "switch"
		data = {'page':page}
		print self.get(url, data)

	def _test_switch_put(self):

		switch_id = 2
		status = 1
		url = REMOTE_URL+ "switch"
		data = {'switch_id':switch_id,'status':status}
		print self.delete(url, data)

	def etag_get(self,url, data):
		data = urllib.urlencode(data)
		full_url = url + '?' + data
		req = urllib2.Request(full_url)
		#使用'8f475faacbd75cbfdc746d6ca10813e7230cd4cc'会报200，格式不同
		req.add_header('If-None-Match','"8f475faacbd75cbfdc746d6ca10813e7230cd4cc"')
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(req)
		return str(response.info())+response.read()

	def _test_etag_switch_get(self):
		page = 1
		url = REMOTE_URL + "switch"
		data = {'page':page}
		print self.etag_get(url, data)

if __name__ == '__main__':
	unittest.main()
