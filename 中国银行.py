

import random
# 1.准备数据库和开户行名称
users={}
'''
    "张三"：{
        "account":"adfadfa",
        "password":"asdfasdf"
    }
'''
bank_name = "中国工商银行昌平支行"
def getRandom():
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0,len(li) - 1)]
        string = string +  ch
    return string
# 银行开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 1.看银行是否已满  满了返回3
    if len(users) > 100:
        return 3

    # 2.用户名是否存在，若存在返回2
    if username in users.keys():
        return 2
    # 3.正常开户，将用户信息存在数据库
    users[username]  = {
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1


# 用户操作逻辑
def addUser():
    username = input("请输入用户名:")
    password = input("请输入取款密码:")
    country= input("请输入国家:")
    province = input("请输入省份：")
    street =  input("请输入街道：")
    door = input("请输入门牌号：")
    account = getRandom()#str(random.randint(10000000,99999999))  #  8888  --> "8888"
    # 架构数据传输给银行
    status = bank_addUser(account,username,password,country,province,street,door)

    if status == 1:
        print("开户成功！以下是您的个人信息：")
        info = '''
            -------------------个人信息------------------
            用户名:%s,
            密码：%s,
            账号:%s,
            地址：
                国家:%s,
                省份:%s,
                街道：%s,
                门牌号:%s
            余额：%s,
            开户行:%s
        '''
        print(info % (username,password,account,country,province,street,door,users[username]["money"],bank_name))

    elif status == 2:
        print("该用户已存在，别瞎弄！")
    elif status == 3:
        print("对不起，数据库已满！请携带证件到其他银行办理！")

def welcome():
    print("--------------------------------------")
    print("-           中国工商银行账户管理系统    -")
    print("--------------------------------------")
    print("-    1.开户                           -")
    print("-    2.存钱                           -")
    print("-    3.取钱                           -")
    print("-    4.转账                           -")
    print("-    5.查询                           -")
    print("-    6.Bye！                          -")
    print("- -------------------------------------")
# 存钱
def cunqian():
    zhanghu=input("请输入用户账号：")
    jine=input("请输入用户金额：")
    jine=int(jine)
    for i in users.keys():
        if zhanghu == users[i]['account']:
            users[i]['money']=users[i]['money']+jine
            print("当前余额为：",users[i]['money'])
            return True
    return False
#取钱
def takeUser():
   takeAccount=input("请输入用账号：")
   if takeAccount in users.keys():
      print("用户正确")
      takePassword = input("请输入密码：")
      if takePassword == users[takeAccount]["password"]:
          print("密码正确")
          takeMoney = input("请输入取钱金额：")
          if takeMoney.isdigit():
              takeMoney = int(takeMoney)
              if takeMoney < users[takeAccount]['money']:
                  users[takeAccount]["money"] = int(users[takeAccount]['money']) - takeMoney
                  print("取钱成功，余额为：", users[takeAccount]["money"])
              else:
                  print("余额不足，请减小取款金额")
      else:
          print("密码输入错误，请重新输入")
   else:
      print("账户输入错误，请重新输入")


# 银行取钱
def bank_getmoney(name,m):
    users[name]["money"] = int(users[name]["money"])-int(m)
#银行存钱，修改账户余额操作
def bank_addmoney(name,m):
    users[name]["money"] =  users[name]["money"]+int(m)
# 用户存在判断
def can(name,word):
    if name in users.keys():
        if word==users[name]["password"]:
            return 0
        else :
            return 2 #密码不正确
    else :
        return 1  #用户不存在
#用户存在和余额判断
def can1(name,word,m):
    m=int(m)
    mon=int(users[name]["money"])
    if name in users.keys():
        if word==users[name]["password"]:
            if m<=mon:
                return 4
            else :
                return 3
        else :
            return 2 #密码不正确
    else :
        return 1  #用户不存在


#转账
def throwmoney():
    def throwmoney():

        name = input("请输入转出账户用户名")
        word = input("请输入转出账户密码")
        m = input("请输入转出金额")
        if can1(name, word, m) == 4:
            nam = input("请输入转入账户用户名")
            wor = input("请输入转入账户密码")
            if can(nam, wor) == 0:
                bank_addmoney(nam, m)
                bank_getmoney(name, m)
                print("向", nam, "账户存入", m, "元", "现存余额为", users[nam]["money"], "元")
                print("向", name, "账户取出", m, "元", "现存余额为", users[name]["money"], "元")

#账户信息查询
def getinformation():
    name = input("请输入用户名")
    word = input("请输入密码")
    if can(name, word)==1:
        print("该用户不存在")
    elif can(name, word) == 2:
        print("密码错误")
    else :
        print("以下是您查询的个人信息：")
        info = '''
                   -------------------个人信息------------------
                   用户名:%s,
                   密码：%s,
                   账号:%s,
                   地址：
                       国家:%s,
                       省份:%s,
                       街道：%s,
                       门牌号:%s
                   余额：%s,
                   开户行:%s
               '''
        print(
            info % (name, users[name]["password"],users[name]["account"] , users[name]["country"], users[name]["province"], users[name]["street"], users[name]["door"], users[name]["money"], bank_name))

while True:
    welcome() # 打印页面
    chose = input("请输入您的业务编号:")
    if chose == '1':
        addUser()
    elif chose == '2':
        cunqian()
    elif chose == '3':
        takeUser()
    elif chose == '4':
        pass
    elif chose == '5':
        pass
    elif chose == '6':
        pass
    else:
        print("输入非法，请重新输入！")







