# -*- coding: utf-8 -*-

import socket

#perazzo = '10.0.47.130'
HOST = '10.0.47.' + input("3:")
#HOST = '127.0.0.1'
PORT = int(input("porta: "))

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    tcp.send(bytes(msg, 'utf-8'))
    msg = input()

tcp.close()