#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-27 15:11:13
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-26 18:48:02


import sys
sys.path.append('..') #导入上级目录到搜索路径
import re

def testRE():
	#all=re.compile('(\d+\.\d+[eE][-+]?\d+|\d+\.\d+|[1-9]\d*|0[0-7]+|0x[0-9a-fA-F]+|[a-zA-Z_]\w*|==|=|!=|&&|\|\||>=|<=|>|<)')

	all = re.compile('(>=|<=|>|<|!=|==|=)')

	#mth=all.findall('temperature >= -10 && humidity == 10 || humidity == 11')
	mth = all.findall('>10 , =19 ,!=11,<1,==12,>12')
	print mth

def json(obj_dict):
		print obj_dict
		return dict((key, obj_dict[key]) for key in obj_dict if re.search("^_|password|_time$",key) == None )



if __name__ == '__main__':
 	#testRE()

	obj_dict = {"create_time":"123"}

	print json(obj_dict)

 	pass
