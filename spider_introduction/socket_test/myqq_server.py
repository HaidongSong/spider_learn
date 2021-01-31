"""
模拟qq登陆
转发消息
处理登陆
处理退出
维护在线用户、历史消息

"""

import socket
from collections import defaultdict
import threading
import json


# 维护在线用户
online_users = defaultdict(dict)

# 维护历史消息
user_msgs = defaultdict(list)

server = socket.socket()
server.bind(("0.0.0.0", 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        json_data = json.loads(data.decode('utf8'))
        action = json_data.get('action', '')
        if action == 'login':
            online_users[json_data['user']] = sock
            sock.send('登陆成功'.encode('utf8'))
        elif action == 'list_user':
            # 获取当前用户数
            all_users = [user for user, sock in online_users.items()]
            sock.send(json.dumps(all_users).encode('utf8'))
        elif action == 'history_msg':
            sock.send(json.dumps(user_msgs.get(json_data['user'], [])).encode('utf8'))
        elif action == 'send_msg':
            if json_data['to'] in online_users:
                # 转发的实现
                online_users[json_data['to']].send(json.dumps(json_data).encode('utf8'))
                # user_msgs[json_data['to']].append(json_data)
                # 往前提一行才能接收离线消息
            user_msgs[json_data['to']].append(json_data)
        elif action == 'exit':
            del online_users[json_data['user']]
            sock.send('退出成功'.encode('utf8'))



while True:
    # 接受阻塞
    sock, addr = server.accept()

    # 给客户端创建一个线程去处理
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

# 1 多线程处理了每个用户的连接，避免消息阻塞
# 2 自定义了消息协议，并且解析了协议






