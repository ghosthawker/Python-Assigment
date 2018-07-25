#!/usr/bin/env python3
import socket, os, time, sys

def Main():
    host = '127.0.0.1'
    port = 5000
    if(len(sys.argv)==2):
        s = socket.socket()
        s.connect((host, port))

        filename = sys.argv[1]
        if filename != 'q':
            s.send(filename.encode('utf-8'))
            data = s.recv(1024)
            print("File Recieve displaying content:")
            print(data)
        s.close()
    else:
        print("Usage ./client <city_name>")

if __name__ == '__main__':
    Main()