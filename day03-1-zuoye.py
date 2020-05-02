#1. 使用多线程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码    生产者产生请求 消费者 要使用队列
#2. 使用多进程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码 思考题
#3.get和post方法的区别
#4. post请求有哪几种数据格式
#https://github.com/xuxuchao/zuoye/blob/master/New_File.py

import threading
import requests
import queue
bingFa=5  #10个并发用户
requestsCount=10 #请求数10
lock = threading.Lock() #创建锁
url = 'http://www.baidu.com'
q= queue.Queue()  #创建队列
requestResultCode=[] #创建一个列表 保持请求响应码

def requestBaidu(url):  #请求百度
    while True:
        try:
            q.get(block=False)   #队列方式拿走数据，队列为空 退出循环
        except queue.Empty:
            break

        with lock:   #确保每次只有一个线程占有锁,使用with方式自动解锁
            r = requests.get(url=url) #请求百度
            requestResultCode.append(r.status_code) #把响应码加到空列表中
        q.task_done()  # 向任务完成队列发送信号  每次get完后都需要掉task_done 直到所有列队都完成
for a in range(requestsCount):  #请求放入队列中
    q.put(a)

for a in range(bingFa):
    #每个并发用户去队列里取值
    t = threading.Thread(target=requestBaidu, args=(url,))
    t.start()    #创建并发用户数（线程），启用
q.join()   #等待队列里的线程都执行完 再执行主线程：打印结果
print (requestResultCode)   #[200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

#get和post方法的区别
# 1、	缓存:get会被浏览器主动缓存,post不会,除非手动设置;
# 2、	安全:get请求参数在url中,不安全,post请求参数在body中;
# 3、	请求参数类型:get只接受ASCII字符，而POST没有限制;
# 4、	大小：Get传输的数据量小，主要是因为它受约于URL长度的限制，而Post可以传输大量的数据，所以我们在传文件的时候会用Post；
# 5、	方式：get是查询数据,post提交修改数据;
# 6、	后退页面的反应：get请求页面后退时，不产生影响,post请求页面后退时，会重新提交请求
#
# post请求有哪几种数据格式
# •	application/x-www-form-urlencoded 表单 如登录
# •	multipart/form-data  上传文件
# •	application/json  json数据
# •	text/xml    xml数据 webserver类型接口
