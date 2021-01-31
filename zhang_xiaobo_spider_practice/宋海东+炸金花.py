# coding=utf-8
import random


def deal():  # 发牌
    a = ["黑桃", "梅花", "红桃", "方片"]
    b = list(range(2, 15))  # 14相当于A
    c = [[color, num] for color in a for num in b]
    random.shuffle(c)
    poker_type = {}
    for p in range(1, 6):
        poker = random.sample(c, 3)
        poker_type['playler' + str(p)] = poker
        map(lambda x: c.remove(x), poker)
        print(f"player{p}:{poker}")
    return poker_type


def compare_two_num(a, b):
    a_list = [i[1] for i in a]
    b_list = [j[1] for j in b]
    a_list.append(a[0][1])
    if a_list > b_list:
        return 1
    elif a_list < b_list:
        return 0
    elif a_list == b_list:
        return 3


def compare_two_pai(a, b):
    """
    a > b. return 1
    a < b. return 0
    a = b. return 3
    :param a:
    :param b:
    :return:
    """
    a = a[1]
    b = b[1]
    if (a[0][1] == a[1][1] == a[2][1]) or (b[0][1] == b[1][1] == b[2][1]):  # 豹子
        if (a[0][1] == a[1][1] == a[2][1]) and not (b[0][1] == b[1][1] == b[2][1]):
            return 1
        elif not (a[0][1] == a[1][1] == a[2][1]) and (b[0][1] == b[1][1] == b[2][1]):
            return 0
        elif (a[0][1] == a[1][1] == a[2][1]) and (b[0][1] == b[1][1] == b[2][1]):
            return compare_two_num(a, b)
    elif (a[0][0] == a[1][0] == a[2][0]) or (b[0][0] == b[1][0] == b[2][0]):  # 同花
        if (a[0][1] - a[1][1] == a[1][1] - a[2][1] == 1) or (b[0][1] - b[1][1] == b[1][1] - b[2][1] == 1):  # 同花顺
            if (a[0][1] - a[1][1] == a[1][1] - a[2][1] == 1) and not (b[0][1] - b[1][1] == b[1][1] - b[2][1] == 1):
                return 1
            elif not (a[0][1] - a[1][1] == a[1][1] - a[2][1] == 1) and (b[0][1] - b[1][1] == b[1][1] - b[2][1] == 1):
                return 0
            elif (a[0][1] - a[1][1] == a[1][1] - a[2][1] == 1) and (b[0][1] - b[1][1] == b[1][1] - b[2][1] == 1):
                return compare_two_num(a, b)
        else:
            return compare_two_num(a, b)
    elif (a[0][1] == a[1][1] or a[1][1] == a[2][1]) or (b[0][1] == b[1][1] or b[1][1] == b[2][1]):  # 对子
        if (a[0][1] == a[1][1] or a[1][1] == a[2][1]) and not (b[0][1] == b[1][1] or b[1][1] == b[2][1]):
            return 1
        elif not (a[0][1] == a[1][1] or a[1][1] == a[2][1]) and (b[0][1] == b[1][1] or b[1][1] == b[2][1]):
            return 0
        elif (a[0][1] == a[1][1] or a[1][1] == a[2][1]) and (b[0][1] == b[1][1] or b[1][1] == b[2][1]):
            return compare_two_num()
        return compare_two_num(a, b)
    else:
        return compare_two_num(a, b)


def compare_poker(pai):
    for i in pai:
        pai[i] = sorted(pai[i], key=lambda x: x[1], reverse=True)  # 整牌， 按数字排序(把字典里的的tuple元素排序)
    list_pai = list(zip(pai, pai.values()))  # dict to list
    for j in range(len(list_pai)):  # 冒泡排序
        for k in range(len(list_pai) - j - 1):
            if compare_two_pai(list_pai[k], list_pai[k + 1]) >= 1:  # True 大于
                list_pai[k], list_pai[k + 1] = list_pai[k + 1], list_pai[k]
    list_pai.reverse()
    return list_pai


print("开始发牌，注意14为A：")
pai = deal()
print("比较牌的大小，由大到小排序！！！")
win = compare_poker(pai)
print(win)
print(50*'=')
print(f'恭喜“{win[0][0]}”，获胜！！！获胜牌型为{win[0][1]}')

