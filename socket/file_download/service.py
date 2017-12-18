import json
import os
import socket

# 实例化出一个服务机器，使用网络传输，使用tcp协议
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定ip和端口
sever.bind(('127.0.0.1', 8090))
# 限制等候接听客户为5
sever.listen(5)
print('running...')


def pack_head(head_dict, head_dict_size):
    bytes_head = bytes(json.dumps(head_dict), encoding='utf-8')
    if len(bytes_head) < head_dict_size:
        head_dict['fill'].zfill(head_dict_size - len(bytes_head))
        bytes_head = bytes(json.dumps(head_dict), encoding='utf-8')
    return bytes_head

while True:
    # 等待接听
    conn, address = sever.accept()

    while True:
        # 接收指令
        res = conn.recv(1024)  # get a.txt
        cmd, filename = res.decode('utf-8').splite()
        if cmd == 'get':
            if os.path.isfile(filename):
                head_dict = {}
                head_dict['filename'] = filename
                head_dict['file_size'] = os.path.getsize(filename)
                head_dict['fill'] = ''
                bytes_head = pack_head(head_dict, 300)

                conn.send(bytes_head)

                with open(filename, 'rb') as f:
                    for line in f:
                        conn.send(line)
                    else:
                        print('file send done...')


conn.close()