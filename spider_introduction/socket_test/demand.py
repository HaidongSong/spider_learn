# 登陆
# 发送消息
# 获取用户列表
# 历史消息
# 退出


# 登陆
login_template = {
    "action": "login",
    "user": "dylan"
}

# 发送消息格式
send_msg_template = {
    "action": "send_msg",
    "to": "user",
    "from": "dylan1",
    "data": "I am dylan"
}

# 在线用户
get_user_template = {
    "action": "list_user",
}

# 历史消息
offline_msg_template = {
    "action": "history_msg",
    "user": "user"
}

# 退出
exit_template = {
    "action": "exit",
    "user": ""
}