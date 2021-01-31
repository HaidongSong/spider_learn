#socekt 服务端

import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0', 8000))
server.listen()



# data = ""


def handle_sock(sock, addr):
    sock.send("Welcome to server!".encode("utf8"))
    while True:
        data_tmp = sock.recv(1024)
        print("Client response:{}".format(data_tmp.decode("utf8")))
        ser_input = input()
        sock.send(ser_input.encode("utf8"))
while True:
    # 阻塞接受等待
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

# while True:

    # data_tmp = sock.recv(1024)
    # print(data_tmp.decode("utf8"))
    # if data_tmp:
    #     data += data_tmp.decode("utf8")
    #     if data_tmp.endswith("#".encode("utf8")):
    #         break
    # else:
    #     break
# print(data)
# server.close()