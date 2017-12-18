import socket
import subprocess

# 实例化出一个服务机器，使用网络传输，使用tcp协议
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定ip和端口
sever.bind(('127.0.0.1', 8090))
# 限制等候接听客户为5
sever.listen(5)
print('running...')
# 等待接听
conn, address = sever.accept()

while True:
    # 接收数据，限制接收的大小
    res = conn.recv(1024)
    if not res:
        break

    cmd = subprocess.Popen(res.decode('utf-8'),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    stdout = cmd.stdout.read()
    stderr = cmd.stderr.read()
    res = stdout + stderr

    if not res:
        res = b'nothing output'

    conn.send(bytes(str(len(res)), encoding='utf-8'))
    conn.recv(1)
    # 将转化后的二进制发送给客户端
    conn.sendall(res)

conn.close()