import requests
from bs4 import BeautifulSoup
import queue
import threading

start_page = "http://www.163.com"
domain = "163.com"  #只爬域名含163.com
url_queue = queue.Queue() #定义一个队列
seen = set()  #集定义一个集合 和列表类似，但元素不能重复 避免爬虫陷入死循环

seen.add(start_page)  #把首页加到集合里，下次出现首页就不爬
url_queue.put(start_page) #把首页加到队列里，让他开始怕


def sotre(url):  #存储集合结果  暂时不做，所以pass  可以加个写文件东西把结果写下来
    pass

def extract_urls(url): #解析网页 把里面url都解析出来
    urls = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    for e in soup.findAll('a'):
        url = e.attrs.get('href', '#')  #取出url  href 如果没有值，给一个默认值#
        urls.append(url) #把链接地址放到urls里
    return urls


def pachongTheadding():
    while True:

        if not url_queue.empty():  #如果队列里有url不会退出 没有才会退出

            current_url = url_queue.get()
            print(current_url)
            sotre(current_url)   #保存爬的url
            for next_url in extract_urls(current_url): #把解析的url迭代  不在集合里，就加到队列里
                if next_url not in seen and domain in next_url:  #不在队列里并且域名163.com结尾 就把他加到队列里 再加到集合里
                    seen.add(next_url)
                    url_queue.put(next_url)
        else:
            break
for i in range(10):#使用多线程并行10次
    t=threading.Thread(target=pachongTheadding)
    t.start()