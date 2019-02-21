#!/usr/bin/python
import socket
ping = socket.socket()
ip = "35.157.111.68"
port = 10151
ping.connect((ip,port))
ping.recv(80)
while True:
	ans = ping.recv(80)
	print ans
	new_ans = ans.split(" ")
	number = new_ans[-1]
	ping.send(number)
	if number:
		print number
	else:
		print ans
		break
