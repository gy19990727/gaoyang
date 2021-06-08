# sum=0
# i=0
# b=0
# while i<10:
#     num = input("请输入数字：")
#     num = int(num)
#     sum =sum +num
#     i = i+1
#     if num>b:
#         b=num
# print(sum)
# print (sum/10)
# print(b)

#
# import random
# a=random.randint(50,150)
# print(a)


# a=int(input("请输入都一条边长"))
# b=int(input("请输入第二条边长"))
# c=int(input("请输入第三条边长"))
# d=[a,b,c]
# if a==b==c:
#     print("d是等边三角形")
# elif a==b or b==c or c==a:
#     print("d是等腰三角形")
#
# elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
#     print("d是直角三角形")
# elif a+b>c or b+c>a or c+a>b:
#     print("d是普通三角形")
# else:
#     print("不能构成三角形")

#
# a=56
# b=78
# c=(a+b)
# a=(c-a)
# b=(c-b)
# print(a)
# print(b)


# name = "root"
# password = "admin"
# i=1
# while i<=3:
#     a = input("请输入用户名：")
#     b = input("请输入用户名密码：")
#     if a== name and b==password:
#         print("密码输入成功，成功登陆系统")
#         break
#     elif a!=name or b!=password:
#         print("用户名或密码输入错误，登陆失败")
#         i = i + 1
#     if i>3:
#         print("输入次数超过三次，系统锁定")
#         break



# num=0
# i=1
# while i<101:
#  num=i+num
#  i=i+1
#  print("1至100的和为：",num ,i-1)

# depth=20
# up=3
# down=2
# remain=depth-up
# times=remain//(up-down)
# times=times+1
# print(times)


# names =["北京","上海","广东"]
# names.append("天津")
# names.append("重庆")
# names.append("哈尔滨")
# names.append("银川")
# names.append("郑州")
# names.append("济南")
# names.append("太原")
# names.append("合肥")
# names.append("长春")
# names.append("沈阳")
# names.append("呼和浩特")
# names.append("石家庄")
# names.append("乌鲁木齐")
# names.append("兰州")
# names.append("西宁")
# names.append("西安")
# names.append("长沙")
# names.append("武汉")
# names.append("南京")
# names.append("成都")
# names.append("贵阳")
# names.append("昆明")
# names.append("南宁")
# names.append("拉萨")
# names.append("杭州")
# names.append("南昌")
# names.append("广州")
# names.append("福州")
# names.append("台北")
# names.append("海口")
# names.append("香港")
# names.append("澳门")
# print(names)
# names[1]="广东"
# names[2]="上海"
# print(names)
# a=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# c=(sum(a))
# print(c)
# b=(c//8)
# print(b)


# a=[1,5,21,30,15,9,30,24]
# a.pop(0)
# a.pop(1)
# a.pop(3)
# a.pop(4)
# b=sum(a)
# print(b)
