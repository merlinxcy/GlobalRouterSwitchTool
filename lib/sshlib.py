import sys
import os
import time
from paramiko import SSHClient
from paramiko import AutoAddPolicy
class sshlib:
	def BruteForce(hostname,port,username,password):
		ssh = SSHClient()
		ssh.set_missing_host_key_policy(AutoAddPolicy())
		try:
			ssh.connect(hostname, port, username, password, pkey=None, timeout = None, allow_agent=False, look_for_keys=False)
			status = 'ok'
			ssh.close()
		except Exception, e:
			status = 'error'
			pass
		return status