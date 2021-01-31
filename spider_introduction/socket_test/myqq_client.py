import socket
import json
import threading

user = 'dylan1'
exit_flag = False

# 0登陆
login_template = {
    "action": "login",
    "user": user
}
client = socket.socket()
client.connect(('127.0.0.1', 8000))
client.send(json.dumps(login_template).encode('utf8'))
res = client.recv(1024)
res = res.decode('utf8')
print(res)

# 1当前登录用户
get_user_template = {
    "action": "list_user",
}
client.send(json.dumps(get_user_template).encode('utf8'))
res = client.recv(1024)
print('当前在线用户：{}'.format(res.decode('utf8')))

# 2历史消息
offline_msg_template = {
    "action": "history_msg",
    "user": user
}
client.send(json.dumps(offline_msg_template).encode('utf8'))
res1 = client.recv(1024)
res1 = res1.decode('utf8')
print("历史消息：{}".format(res1))


def handle_recv():
    while True:
        if not exit_flag:
            try:
                res_msg = client.recv(1024)
                # res_msg = res_msg.decode('utf8')
                # 不能写在这里，不能获得在线用户数据
            except:
                break
            res_msg = res_msg.decode('utf8')
            try:
                res_msg = json.loads(res_msg)
                from_user = res_msg['from']
                from_data = res_msg['data']
                print(' ')
                print('收到来自({})的消息：{}'.format(from_user, from_data))
            except:
                print(' ')
                print(res_msg)
        else:
            break


def handle_send():
    # 3发送接收消息
    while True:
        # 随时可以发送消息
        # 有新消息实时接收
        op_type = input('请输入你的操作：1.发送消息  2.退出  3.查看在线用户:')
        if op_type not in ['1', '2', '3']:
            print('不支持该操作，请重新输入：')
            op_type = input('请输入你的操作：1.发送消息  2.退出  3.查看在线用户:')
        elif op_type == '1':
            to_user = input('请输入接受者：')
            msg = input('请输入要发送的消息  ')
            send_msg_template = {
                "action": "send_msg",
                "to": to_user,
                "from": user,
                "data": msg
            }
            client.send(json.dumps(send_msg_template).encode('utf8'))
        elif op_type == '2':
            # 4退出
            exit_template = {
                "action": "exit",
                "user": ""
            }
            client.send(json.dumps(exit_template).encode('utf8'))
            # 其他用户能够关闭另一个用户，解决办法：
            # 1服务端for循环遍历要退出用户的sock，确认时这个用户，再退出
            # 2最开始的时候用socket生成一个不变字符串，退出的时候根据获得的sock反向生成字符串，做一个对比。。。

            exit_flag = True
            client.close()
            break
        elif op_type == '3':
            get_user_template = {
                "action": "list_user",
            }
            client.send(json.dumps(get_user_template).encode('utf8'))


if __name__ == '__main__':
    send_thread = threading.Thread(target=handle_send)
    recv_thread = threading.Thread(target=handle_recv)
    send_thread.start()
    recv_thread.start()
