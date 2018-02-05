# -*- coding:utf-8 -*-

import socket
port = 8081
host = "localhost"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("", 0))
s.sendto("Holly Guido! It's working.", (host, port))