#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-27 14:16:30
# @Last Modified by:   shiningchan
# @Last Modified time: 2014-01-27 21:51:11

import os, sys, time
from signal import SIGTERM

class BaseDaemon():

	def __init__(self,pidfile,stdin='dev/null',stdout='dev/null',stderr='dev/null'):
		self.pidfile = pidfile
		self.stdin = stdin
		self.stdout = stdout
		self.stderr = stderr

	def daemonize(self):

		#脱离父进程
		try:
			pid = os.fork()
			if pid > 0:
				sys.exit(0)
		except OSError,err:
			sys.stderr.write("Fork 1 has failed --> %d -- [%s]\n" % (err.errno,err.strerror))
			sys.exit(1)

		os.chdir('/') 	#修改当前工作目录
		os.setsid()		#脱离终端
		os.umask(0)		#重设文件创建权限

		try:
			pid = os.fork()
			if pid > 0:
				print "Daemon process pid %d" % pid
				sys.exit(0)
		except OSError, err:
			sys.stderr.write("Fork 1 has failed --> %d -- [%s]\n" % (err.errno,err.strerror))
			sys.exit(1)
		
		#重定向IO和错误
		sys.stdout.flush()
		sys.stderr.flush()
		si = file("/dev/null",'r')
		so = file("/dev/null",'a+')
		se = file("/dev/null",'a+',0)
		os.dup2(si.fileno(), sys.stdin.fileno())
		os.dup2(so.fileno(), sys.stdout.fileno())
		os.dup2(se.fileno(), sys.stderr.fileno())


	def start_daemon(self):

		try:
			pf = open(self.pidfile, 'r')
			pid = int(pf.read().strip())
			pf.close
		except IOError:
			pid = None

		if pid :
			ms = "pidfile %s already exist, daemon is running \n"
			sys.stderr.write(ms % self.pidfile)
			sys.exit(1)

		self.daemonize()
		self.run()

	def stop_daemon(self):
		try:
			pf = open(self.pidfile, 'r')
			pid = int(pf.read().strip())
			pf.close
		except IOError:
			pid = None

		if not pid:
			ms="pidfile %s does not exit,daemon not running\n"
			sys.stderr.write(ms % self.pidfile)
			return

		try:
			while 1:
				os.kill(pid,SIGTERM)
				time.sleep(0.1)
				os.remove(self.pidfile)
		except OSError,err:
			err = str(err)
			if err.find('No such process') > 0:
				if os.path.exists(self.pidfile):
					os.remove(self.pidfile)
				else:
					print str(err)
					sys.exit(1)

	def restart(self):
		self.stop_daemon()
		self.start_daemon()

	def run(self):
		"""override to run your own funcation"""		
		pass