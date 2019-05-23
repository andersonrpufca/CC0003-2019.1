# -*- coding: utf-8 -*-

import socket

HOST = ''
PORT = 5003

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

print("rodando")
while True:
    con, client = tcp.accept()
    print('Conectado por ', client)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(client, msg)
    print('Finalizando conexao do cliente', client)
    con.close()