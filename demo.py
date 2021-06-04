'''
    猜数字：
    需求：
        1.猜的数字是系统产生，不是自己定义
            使用random随机数技术来获取随机数
        2.键盘输入
            input("提示")
        3.循环
            while条件循环
            开始，结束，自增，任务
        4.判断
            if 判断条件  elif 判断条件.......else
    范围：0~150
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxxx。
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。10次没猜中，系统锁定。猜中加3000。
'''
import random
# 1. 让系统产生一个随机数
num = random.randint(0,150)
money= 5000
# 开始输入您要猜的数。
i = 0
while i < 15:
    # 任务：输入数据并比对数据
    number = input("请输入您要猜的数：")
    number = int(number)  # "56"  -->  56
    if i<10:
        if number > num:
            money = money - 500
            print("大了！金额还剩：",money)
        elif number < num:
            money = money - 500
            print("小了！金额还剩：",money)
        elif number==num:
            money = money + 3000
            print("恭喜猜中！本次数字为：",num,"金额奖励3000，金额还剩：",money)
            # 跳出训话
            break # 跳出循环
    elif i>=10:
        print("输入的次数超过十次，系统锁定")
        break

    i= i + 1  # 每次加1x   








