# import requests
# # cookies = '_octo=GH1.1.1849343058.1576602081; _ga=GA1.2.90460451.1576602111; __Host-user_session_same_site=nbDv62kHNjp4N5KyQNYZ208waeqsmNgxFnFC88rnV7gTYQw_; _device_id=a7ca73be0e8f1a81d1e2ebb534
# cookies = '_octo=GH1.1.2102186213.1611147634; tz=Asia%2FShanghai; _device_id=a1bbc1f25584d7ece48ecdcb742cd1be; has_recent_activity=1; user_session=VebwY76pVAddm6Bfg0-3xkQqgC3ea_L0xardPtQgcuZpu7Lb; __Host-user_session_same_site=VebwY76pVAddm6Bfg0-3xkQqgC3ea_L0xardPtQgcuZpu7Lb; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=HaidongSong; _gh_sess=WL5OAimgRUwm8ZWxIvdZ%2FgDPG8RGc2K40%2FEbXa01Iq4BjHIB%2Bg4CsT2EVD8sr97VNnXoZPQqPTxjRrmy1H%2FAZvhWO1H%2F2eb4hDTH2gHkn03DU4yxld8r7%2FraF44DIkNZYHG9tel3KLDNRxPVr1TDqQmZabpiDeaVqT4yTAy8%2F1vYYYz0eDjmdyZBmgCO5N%2BQekMLsVJRmbO42R%2BZEdytuyUpX5Et3YPQPDMkyevg52A8o2duGjoLqoadtJaEh6ZI6lzfGXNTe2mM9hXZYIQq4CNvkCVDt7ywQU3PKVZEEtdaiTDvebeEKNDAtH%2FJItIX9tnBtRzqGTFGMQ6g6FNtsG1Nvl7IKD0xOXbot3fEPWsVwy6NZ4hzl87t1TTOGrPR%2Fge0O6XSNPG8ol27FbJg6Nc%2F%2BKdofoqau7cLs9r2QKwkryLleLFqUaPyfs7eMrrJmSBDTWZ%2Bz4jp9BmRpqayOejOkl9XtM%2FF16RZ4GmBU8i757bQDD59k0k9qKmor2UJclXqfDws0%2BlEEeW8nKgRlCUhM65qsD4ivUMfVommTtcfTw26DehVJIwNOg98KApbDDwE1CDh%2F8z%2FNGCjJlHOzwks0BmyaqZSGBdzIEfeCGqJDdqWpsxqHE%2BLuwAIHsnvl7W8tWWC3g%2BOeZ9B81qzdiiLJwGS0%2FGPqpAOg8j0x6r999wG%2FrUKkFG61tPolSK19DL1pG5UemqbJwS7oosRpsgXUkbyWt9vtPkjmqEGILcwh2CnD6ya0Qgbcg9vQVagZshm92SG0%2BytPYQpQTNHU0hhxj%2B6Dk6Vf9RQmIy4LCsO8Y0dUoSfXp7sXuT%2FvR6JPs4LnPnJNInIPQZKD8U2W0nwtGzpWdGbEO%2BJ%2FsdEA6L8UGrw7hcoP5offZ26qt8zanrdv6l9c%2Fjw3SA%2BxZmVMw3fWxzoUuniNa5ZSiyq%2Bis%3D--CIVU9ME8Wzc0YqNn--XKtBu%2ByLRARTFdT6RciRkg%3D%3D'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
# print(cookies.split(';'))
# for cookie in cookies.split(';'):
#     print(cookie.split('=', 1))
#     key, value = cookie.split('=', 1)
#     print(key, value)
# jar.set(key, value)
# r = requests.get('https://github.com/', cookies=jar, headers=headers)
# print(r.text)

# a, b, c = [1, 2, 3]
# print(set(a, b))


# import requests
# data = {'name': 'germey', 'age': '25'}
# r = requests.get("http://httpbin.org/post", params=data)
# print(r.text)


# import os
# print(os.path.dirname(__file__))
#
# a = {
#     1: 2,
#     2: 0,
#     4: 9
# }
# print(list(a.values()))

# import multiprocessing
# import time
#
#
# def process(index):
#     time.sleep(index)
#     print('process', index)
#
#
# for i in range(5):
#     p = multiprocessing.Process(target=process, args=(i, ))
#     p.start()
# print(f"multimprocess core number:{multiprocessing.cpu_count()}")
#
#
#


# x = 0


# def journey(y):
#     global x
#     x += y
#     return x
#
#
# print(journey(3))
# print(journey(5))
# print(journey(8))
# x = 0
#
#
# def traveler(pos):
#     def journey(y):
#         nonlocal pos
#         sum1 = pos + y
#         pos = sum1
#         return sum1
#
#     return journey
#
#
# f = traveler(x)
# print(f(3))
# print(f(5))
# print(f(6))






# class Student():
#     sun = 'haidong'
#     age = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # print(name, age)
#
#
# a = Student('ppx', 20)
# print(a.__dict__)
# print(Student.sun)


# ort re
#
# origin_str = 'boooooooooooooobbysdfas'
# regex_str = '(b.*?b)'
# match_str = re.match(regex_str, origin_str)
# print(match_str.group(1))

# re.sub('b', 'a', origin_str)
# print(origin_str)



# http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=1&pn=1&rn=30&reqId=615ae920-2d21-11ea-b560-73e04c9f8018



import os
# import sys
# print(__file__)
# print(sys.path)
# print(os.path.dirname())
# from os import system
#
# print(system('df -h'))


# pai = {'playler1': [['梅花', 12], ['方片', 11], ['梅花', 6]], 'playler2': [['黑桃', 8], ['黑桃', 3], ['红桃', 4]], 'playler3': [['红桃', 4], ['方片', 12], ['方片', 8]], 'playler4': [['黑桃', 13], ['方片', 4], ['方片', 6]], 'playler5': [['方片', 6], ['红桃', 14], ['黑桃', 14]]}

# list_pai = list(zip(pai, pai.values()))  # dict to list
# print(list_pai)
# num = [1, 2, 3, 4]
# color = ['red', 'black', 'green', 'white']
# c = [[i, j] for i in color for j in num]
# print(c)


# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c']
#
# print(a + b)
# print(a - b)

# a = {"lisa": 1, "mery": 2, "sansa":3}
# c = a
#
# c["lisa"] = 4
# print(a)
# print(c)

# a = [('playler2', [['红桃', 11], ['方片', 9], ['红桃', 4]]), ('playler3', [['黑桃', 11], ['黑桃', 9], ['梅花', 6]]), ('playler1', [['梅花', 13], ['黑桃', 9], ['红桃', 8]]), ('playler4', [['方片', 13], ['方片', 12], ['黑桃', 5]]), ('playler5', [['黑桃', 14], ['梅花', 8], ['红桃', 4]])]
# aList = [123, 'xyz', 'zara', 'abc', 'xyz']
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# c = [(1, 3), (2, 5), (2, 4), (8, 9), (7, 3), (4,2)]
# list1.reverse()
# aList.reverse()
# a.reverse()
# c.reverse()
# print(a)
# print(aList)
# print(list1)
# print(c)

# m = [1, 2, 3, 4, 5]
# def compare_two_num(a, b):
#     a_list = [i[1] for i in a]
#     b_list = [j[1] for j in b]
#     if a_list > b_list:
#         return 1
#     elif a_list < b_list:
#         return 0
#     elif a_list == b_list:
#         return 3
#
# c = (['梅花',2],['方片',5],['黑桃',10])
# d = (['方片',2],['方片',5],['梅花',19])
# a = compare_two_num(c,d)
# print(a)
# a = (['梅花',2],['方片',4],['黑桃',7])
# b = (['方片',2],['方片',4],['梅花',8])
# print(a < b)


#
# import  collections
# a = collections.OrderedDict()
# a = {'f22': 500, 'jian20': 6000}
# for i in range(len(a)):
#     print(i)
# for i,j, in a.items():
#     print(i,j)
# b = list(a)
# c = list(a.values())
# d = zip(b,c)
#
# print(list(d))









# import sys
# from tkinter import Button,mainloop
#
# x=Button(text='Press me',command=(lambda :sys.stdout.write('Hello,World\n')))
# x.pack()
# x.mainloop()
# a = 1
# b = 1
# if a == b == 1:


# a = [('a', 2), ('c', 4), ('v', 9), ('5', 4)]
# p = sorted(a, key=lambda x: x[0])
# print(p)
# # c = lambda x, y, z: x*y*z
# print(c(2, 3, 4))



# print('a'=='a'=='a'=='a'=='a'=='a')

# import random
# a = ["黑桃", "梅花", "红桃", "方片"]
# b = ["A", "2", "3", "4", "5", "6", "9", "8", "9", "10", "J", "Q", "K"]
# c = []
# for i in a:
#     for j in b:
#         c.append(i + j)
# p = random.sample(c, 3)
# print(c-p)
# a = [1, 2, 3, 4]
# b = [1, 2, 3]
# c = list(set(a) - set(b))
# print(c)

# a = [1,2,3]
# print(enumerate(a))
# b = '1'
# print(b.isdigit())
# def f1(x):
#     return x**2
# # a = list(range(10))
# b = filter(f1, range(10))
# for i in b:
#     print(i)

# print(abs(-11.01))
# a = [1, 2, 3, 0 ]
# print(dir())
# print(locals())

# a = [1,2,3]
# b = [1,2,3,4,5,6]
# print(b-a)


# a = 4
# def f1():
#     global a
#     a = 7
#     print(a)
# f1()
# print(a)
# account = {}
# f = open('file', 'r+')
# for line in f:
#     new_line = line.strip().replace(' ', '').split(',')
#     account[new_line[0]] = new_line
# count = 0
# while True:
#     user = input("Pleash input username:")
#     if user not in account.keys():
#         continue
#     elif account[user][2] == '1':
#         print("account locked!!!")
#         continue
#     else:
#         while count < 3:
#             passed = input("Please input password:")
#             if passed == account[user][1]:
#                 print('success ok!!!')
#                 break
#             else:
#                 print('password failed!!!')
#                 count += 1
#                 continue
#
#         if count == 3:
#             print('your account is locked!!!')
#             account[user][2] = '1'
#             f.seek(0)
#             f.truncate()
#             for j in account:
#                 p = ', '.join(account[j])
#                 f.write(p + '\n')
#             f.close()
#             break
#         break








# import sys
# old_str = sys.argv[1]
# new_str = sys.argv[2]
# f = open('file', 'r+')
# data = f.read()
# count = data.count(old_str)
# new_data = data.replace(old_str, new_str)
# f.seek(0)
# f.truncate()
# f.write(new_data)
# f.close()
# print(f"success replace {old_str} to {new_str}, total {count}")

# f = open('file', 'r+')
# data = f.read()
# new_data = data.replace('你好', 'hello')
# print(new_data)
# f.seek(0)
# f.truncate()
# f.write(new_data)

# f = open('file', 'w')
# f.write('你好a\n')
# f.write('我也好')
# f.write('他好吗')
# f.write('test')
# print(f.tell())
# f.seek(11)
# f.write('sdf')


# import random
# # print(list(range(1, 301)))
# b = random.sample(range(1, 11), 3)
# print(b)
# # c = [i for i in range(1, 301) if i not in b]
# c = set(range(1, 11)) - set(b)
# print(c)
#
# # print(random.sample(c, 3))
# a = [1,3,2]
# b = [5]
# c = a + b
# print(c)