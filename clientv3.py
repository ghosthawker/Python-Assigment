#!/usr/bin/env python3 
import socket, os.path, datetime, sys

if (len(sys.argv)==2 ):

	host = '127.0.0.1'
	port = 50001

	s = socket.socket()
	s.connect((host, port))

	f = sys.argv[1] + '.txt'
	s.send(f.encode('utf-8'))
	s.shutdown(socket.SHUT_WR)
	data = s.recv(1024).decode('utf-8')
	print(data)
	print("See you again!")
	s.close()

else:
	print("Usage: <city_name>")