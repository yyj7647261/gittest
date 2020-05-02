import threading
import time
def hellworld():
    time.sleep(2)
    print ("helloworld")

t=threading.Thread(target=hellworld)    #模块.类(target=函数)    创建一个运行helloworld的线程
t.start()  #开始执行这个helloworld程序
print ("main thread") #先打印main这个线程  hello要等2秒才出结果
print ("---")
import threading
import time
def helloworld(id):
    time.sleep(2)
    print("thread %d helloworld" % id)
for i in range(5):
    t = threading.Thread(target=helloworld, args=(i,))
    t.start()
print("main thread") #main thread  thread 0 helloworld....