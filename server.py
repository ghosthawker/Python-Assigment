#!/usr/bin/env python3
import socket, threading, os, sys



def RetrFile(name, sock):
    filename = sock.recv(1024)
    filename = filename.decode('utf-8')
    with open(filename, 'rb') as f:
        bytesToSend = f.read(1024)
        sock.send(bytesToSend)
        while bytesToSend != "0":
            bytesToSend = f.read(1024)
            sock.send(bytesToSend)
    sock.close()


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print("Server Started.\nWaiting for a connection...")
    while True:
        c, addr = s.accept()
        print("Client connedted ip:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()

    s.close()


if __name__ == '__main__':
    Main()