# 这是一个命令行下的名片管理系统
#The simplest business card management system
#主功能界面
def all_fuc():
    print('   名片管理系统v1.0')
    print('-----------------------')
    print('1：添加名片')
    print('2：删除名片')
    print('3：修改名片')
    print('4：查询名片')
    print('5：显示所有名片')
    print('6：退出系统')
    print('-----------------------')


all_fuc()
mp = []
shuru = input('请输入序号执行：')

# 增加名片
def add_mp(name, age, telephone):
    newmans = {'name': name, 'age': age, 'tel': telephone}
    mp.append(newmans)    
    all_fuc()
    print('名片添加成功！')
    return mp

# 删除名片
def del_mp(name):
    global mp
    dnew = []
    mpnew = {}
    for dn in mp:
        if dn['name'] == name:
            print('删除名片{}成功！'.format(name))
        else:
            dnew.append(dn)
    mp = dnew  
    return mp


# 修改名片
def upd_mp(name):
    global mp
    mpnew = []
    for dn in mp:
        if dn['name'] == name:
            dn['age'] = int(input('修改年龄为：'))
            dn['tel'] = input('修改电话号码为：')
            mpnew.append(dn)
            print('修改后的年龄：{}和电话号码:{}')
        else:
            mpnew.append(dn)
    mp = mpnew
    all_mp()
    all_fuc()


# 查看单个名片
def sel_mp(name):
    global mp
    mpnew = []
    for dn in mp:
        if dn['name'] == name:
            mpnew.append(dn)
            print('您查看{}的年龄为：{}岁，电话号码为:{}'.format(dn['name'], dn['age'], dn['tel']))
    all_fuc()


# 查看所有名片
def all_mp():
    global mp
    mpnew = []
    for dn in mp:
        mpnew.append(dn)
        print('姓名：{}的年龄为：{}岁，电话号码为:{}'.format(dn['name'], dn['age'], dn['tel']))
    all_fuc()

#不停执行程序，输入6才退出系统
while True:
    if shuru == '6':
        exit()
    elif shuru == '5':
        all_mp()
        shuru = ''
    elif shuru == '4':
        name = input('请输入您要查看的用户名：')
        sel_mp(name)
        shuru = ''
    elif shuru == '3':
        name = input('请输入要修改的用户名：')
        upd_mp(name)
        shuru = ''
    elif shuru == '2':
        name = input('请输入要从名片系统删除的用户名：')
        del_mp(name)
        shuru = ''
    elif shuru == '1':
        name = input('请输入姓名：')
        #这里后面还需要加一个输入控制，只让用户输入正整数
        age = int(input('请输入年龄：'))
        tel = input('请输入电话号码：')
        add_mp(name, age, tel)
        all_mp()
        shuru = ''
    else:
        shuru = input('请输入正确的序号执行：')
