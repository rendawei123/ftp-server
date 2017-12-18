#  encoding:utf-8

import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('172.16.249.128', 8899))
server.listen(5)
print('sever running...')

connet, addr = server.accept()

while True:

    data = connet.recv(1024)
    if not data:
        break
    cmd = subprocess.Popen(data.decode('utf-8'),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout = cmd.stdout.read()
    stderr = cmd.stderr.read()
    cmd_res = stdout + stderr
    if not cmd_res:
        cmd_res = b'has not output'

    connet.sendall(cmd_res)

