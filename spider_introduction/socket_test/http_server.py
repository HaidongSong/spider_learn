#socekt 服务端

import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    # sock.send("Welcome to server!".encode("utf8"))
    while True:
        data_tmp = sock.recv(1024)
        print("Client response:{}".format(data_tmp.decode("utf8")))
        ser_input = '''HTTP/1.1 200 OK

<html>
    <head>
        <title>
            Build a web server.
        </title>
    </head>
    <body>
        Hello world! This is very simple html document.
    </body>
</html>                
      
        
'''
        sock.send(ser_input.encode("utf8"))


while True:
    # 阻塞接受等待
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
