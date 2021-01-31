import random
first_prize = "泰国五日游"
second_prize = "Iphone手机"
third_prize = "避孕套一盒"

num = range(1, 301)
print("第一次抽奖：")
third_num = random.sample(num, 30)
print(third_num)
print('恭喜以上同事获得---' + third_prize)

print("第二次抽奖：")
num2 = [i for i in num if i not in third_num]
second_num = random.sample(num2, 6)
print(second_num)
print('恭喜以上同事获得---' + second_prize)

print("第三次抽奖：")
num3 = [i for i in num2 if i not in second_num]
third_num = random.sample(num3, 3)
print(third_num)
print('恭喜以上同事获得---' + first_prize)



