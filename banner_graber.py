#!/bin/python

import socket
import sys

def grab_banner(ip, port):
    socket.setdefaulttimeout(1)
    s = socket.socket()
    s.connect_ex((ip, port))
    banner = s.recv(1024)
    s.close()

    print "{0} GRABED BANNER {0}".format("-"*20)
    print banner

if len(sys.argv) == 3:
    IP = str(sys.argv[1])
    PORT = int(sys.argv[2])
    grab_banner(IP, PORT)
else:
    print "[!] Script was invoked with invalid number of arguments"
    print "[!] Syntax: python banner_graber.py {IP} {PORT}"
