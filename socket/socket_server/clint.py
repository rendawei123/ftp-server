# encoding:utf-8

import socket

clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clint.connect(('172.16.249.128', 8899))

while True:
    msg = input('>>>:')
    if not msg:
        continue

    clint.send(msg.encode('utf-8'))
    response = clint.recv(1024)
    print(response.decode('utf-8'))

clint.close()
