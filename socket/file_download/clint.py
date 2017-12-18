import json
import socket

clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clint.connect(('127.0.0.1', 8090))

while True:
    cmd = input('>>:').strip()
    print(cmd)
    if not cmd:
        continue
    clint.send(cmd.encode('utf-8'))

    msg_head = clint.recv(300).decode('utf-8')
    head = json.loads(msg_head)
    filename = head['filename']
    file_size = head['size']
    with open(filename, 'wb') as f:
        recv_size = 0
        while recv_size < file_size:
            if file_size - recv_size < 1024:
                data = clint.recv(file_size - recv_size)
            else:
                data = clint.recv(1024)
            recv_size += len(data)
            f.write(data)
            print('recv:', recv_size, file_size)

        else:
            print('file receive done ...', filename, file_size)

clint.close()
