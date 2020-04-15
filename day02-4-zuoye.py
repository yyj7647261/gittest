import os
path="D:\gittest"

def f1(path):
    list=[]
    for home,dirs,files in os.walk(path):     #os.walk 返回当前目录 文件夹 文件 以及当前目录下
        for i in files:
            list.append(os.path.join(home,i))   #遍历文件，添加到列表
    return list
if __name__=="__main__":
    a1=f1(path)
    print ("文件数:"+str(len(a1))+"分别是:")
    for b in a1:
        print (b)

