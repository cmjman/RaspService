#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 16:41:14
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-25 17:12:13

import urllib
import urllib2

HOST_URL = "http://127.0.0.1:8080/service/"

def post(url, data):
	req = urllib2.Request(url)
	data = urllib.urlencode(data)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	response = opener.open(req, data)
	return response.read()

def registerTest():
	posturl = HOST_URL + "register"
	data = {'nick':'testUser','password':'123456'}
	print post(posturl, data)

def loginTest():
	posturl = "http://127.0.0.1:8080/service/login"
	data = {'user_id':'1','nick':'testUser','password':'123456'}
	print post(posturl, data)

def addTaskTest():
	posturl = "http://127.0.0.1:8080/service/addTask"
	data = {'user_id':'1','switch_id':'1','target_status':'True','if_expression':''}
	print post(posturl, data)

def addSwitchTest():
	posturl = "http://127.0.0.1:8080/service/addSwitch"
	data = {'name':'switch01','level':'0'}
	print post(posturl, data)

def delSwitchTest():
	posturl = HOST_URL+ "delSwitch"
	data = {'switch_id':'2'}
	print post(posturl, data)

if __name__ == '__main__':
	#registerTest()
	#loginTest()
	#addTaskTest()
	#addSwitchTest()
	delSwitchTest()