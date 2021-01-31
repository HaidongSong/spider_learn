import socket

http_socket = socket.socket()
http_socket.connect(('www.baidu.com', 80))
http_socket.send('GET / HTTP/1.1\r\nConnection:close\r\n\r\n'.encode('utf8'))

data = b''
while True:
    temp = http_socket.recv(1024)
    if temp:
        data += temp
    else:
        break
    print(data.decode('utf8'))

# 课后作业，通过socket模拟HTTPS获取网页数据
