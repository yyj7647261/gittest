#打印出指定目录下的文件个数 文件名
#两种实现方式:1、判断是文件的就递归，是文件夹的就加到列表中;    2、使用os.walk 遍历出所有文件和文件夹 然后加到列表中;
#os.listdir() 列表形式返回当前目录下所有文件和文件夹
import os
path="D:\gittest"

def f(path,list):
   if os.path.isfile(path):
       list.append(path)
   elif os.path.isdir(path):  #是文件夹
       for i in os.listdir(path):#遍历当前的文件夹下所有文件夹和文件夹
           newPath=os.path.join(path,i)
           f(newPath,list)
   return list
if __name__=="__main__":
    a=f(path,[])
    print ("文件数:"+str(len(a))+"分别是:")
    for b in a:
        print (b)








#print (os.listdir(path)) #打印出当前目录下的所有文件和文件夹 ，列表展示
