print("---欢迎使用通讯录欢迎,请输入数字操作")
print("---查询1、修改2、新增3、删除4、退出5、输入其他重新开始")

Txl1={'name':'王一','tel':13826505123,'id':'001'};


def query_record():   #查询通讯录
    print ("查询结果："+str(Txl1))

def change_record():#修改通讯录
    Txl1['name'] = '王五'
    print("修改结果:"+str(Txl1))

def add_record(): #新增通讯录
    Txl2={'name':'李四','tel':13826505124,'id':'004'};
    Txl1['新增'] = Txl2
    print("新增结果:" + str(Txl1))

def delete_record(): #删除通讯录
    del Txl1['新增']
    print("删除结果:" + str(Txl1))

while True:
    a = input('程序启动,请输入数字操作：')
    if a=="1":
        query_record()
    elif a=="2":
        change_record()
    elif a=="3":
        add_record()
    elif a=="4":
        delete_record()
    elif isinstance(a,int)==False:
        print("输入非法，退出程序")
        break
    else:
        print("输入数字有误,退出程序")
        break
print ("程序关闭，请重新开始")





