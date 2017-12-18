import socket

clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clint.connect(('127.0.0.1', 8090))

while True:
    msg = input('>>:').strip()
    print(msg)
    if not msg:
        continue
    clint.send(msg.encode('utf-8'))
    len_res = int(clint.recv(500).decode('utf-8'))
    clint.send(b'1')
    # res = clint.recv(len_res)
    b = b''
    total_size = len_res
    recv_size = 0
    while recv_size < total_size:
        if total_size - recv_size < 1024:
            d = clint.recv(total_size - recv_size)
        else:
            d = clint.recv(1024)
        recv_size += len(d)
        b += d
    print(b.decode('utf-8'))

clint.close()
