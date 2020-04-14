def zhuangshi(method):
    def wra(self):
        print ("你输入的用户名"+self.username+"密码是:"+self.password)
        method(self)
    return  wra

class M:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    @zhuangshi
    def method(self):
        if self.username == "root" and self.password == "123":
            print("你有权限登录")
        else:
            print("你没有权限登录")
if __name__=="__main__":
    p1=M("root","123")
    p1.method()