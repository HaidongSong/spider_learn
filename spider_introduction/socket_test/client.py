#socket 客户端

import socket
client = socket.socket()
client.connect(('192.168.6.130', 8000))
server_data = client.recv(1024)
print("Server reponse: {}".format(server_data.decode("utf8")))

while True:
    date_input = input()
    client.send(date_input.encode("utf8"))
    server_data = client.recv(1024)
    print("Server reponse: {}".format(server_data.decode("utf8")))

# client.close()
