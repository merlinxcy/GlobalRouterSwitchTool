import os
import sys
import shlex
from lib import telnetlibs
from lib import sshlib
class GUI:
	def makefgui():
		pass


class commandline:
	func_code=-1
	host_ip='192.168.237.129'
	host_port=1234
	target_ip='192.168.237.66'
	target_port=''
	SHELL_STATUS_RUN=1
	SHELL_STATUS_STOP=0
	def show_menu(self):
		print '''
		IIIIII    dTb.dTb        _.---._
		II     4'  v  'B   .'"".'/|\`.""'.
		II     6.     .P  :  .' / | \ `.  :
		II     'T;. .;P'  '.'  /  |  \  `.'
		II      'T; ;P'    `. /   |   \ .'
		IIIIII     'YvP'       `-.__|__.-'
		I love shells --egypt

		Welcome to use GlobalRouterSwitchTool!
		Author:Xeldax        mail:xcy_melin@outlook.com
		[1]telnet bruteforce
		[2]ssh bruteforce
		[3]router vulnerability exploit
		[4]switch vulnerability exploit
		[5]arp flood
		[6]arp poison
		[7]dhcp flood
		[8]dhcp posion
		[9]cdp/lldp flood
		[10]stp attack
		[11]vlan hopping attack
		[12]vtp attack
		[13]yersinia
		[0]host alive detect
----------------------------------------
		'''

	def run_exec(self,cmd):
		#sys.stdout.write(cmd)
		print cmd
		#check 1
		if cmd[0]=="exit":
			return self.SHELL_STATUS_STOP
		elif cmd[0]=="set":
			if cmd[1]=="host":
				self.host_ip=cmd[2]
			elif cmd[1]=="target":
				self.target_ip=cmd[2]
		elif cmd[0]=="use":
			if cmd[1]=="1":
				print 1
				a=telnetlibs.telnetlibs(self.target_ip)
				a.run()
				#pass
			elif cmd[1]=="2":
				print 2
				a=sshlib()
				pass
			elif cmd[1]=="3":
				print 3
				pass
			elif cmd[1]=="4":
				print 4
				pass
			elif cmd[1]=="5":
				print 5
				pass
			elif cmd[1]=="6":
				print 6
				pass
			elif cmd[1]=="7":
				print 7
				pass
			elif cmd[1]=="8":
				print 8
				pass
			elif cmd[1]=="9":
				print 9
				pass
			elif cmd[1]=="10":
				print 10
				pass
			elif cmd[1]=="11":
				print 11
				pass
			elif cmd[1]=="12":
				print 12
				pass
			elif cmd[1]=="13":
				print 13
				pass
		else :
			sys.stdout.write("[-]unkown command!")
		
		return self.SHELL_STATUS_RUN




	def shell(self):
		status=self.SHELL_STATUS_RUN
		while  status==self.SHELL_STATUS_RUN:
			sys.stdout.write('>  ')
			sys.stdout.flush()
			cmd=sys.stdin.readline()
			#cmd_tokens=cmd
			cmd_tokens=self.tokenize(cmd)
			status=self.run_exec(cmd_tokens)

	def tokenize(self,cmd):
		return shlex.split(cmd)











if __name__=='__main__':
	a=commandline()
	a.show_menu()
	a.shell()


