import socket
import fcntl
import struct
import uuid
def get_ip_address(ifname):
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	a= socket.inet_ntoa(fcntl.ioctl(\
		s.fileno(),\
		0x8915,\
		struct.pack('256s',ifname[:15])\
		)[20:24])
	return a

def get_mac_address():
	node=uuid.getnode()
	mac=uuid.UUID(int=node).hex[-12:]
	newmac=''
	for i in range(0,len(mac)):
		if i%2!=0 or i==0:#use or is not good in principle
			newmac+=mac[i]
		else:
			newmac+=':'
			newmac+=mac[i]
	return newmac

#print get_mac_address()