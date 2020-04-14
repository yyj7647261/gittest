#  递归函数列出所有文件 使用os.listdir  列出目录内容   os.isfile  检测是否是文件
# 练习找出单个目录中的最大文件
# 练习找出目录树中的最大文件
import os
file=os.listdir() #列出所有文件
# print (type(file))
# print ("当前目录所有文件:"+str(file))  #累出当前目录中的全部文件
# #os.path.getsize(name)    获取文件大小
maxV = -float('inf')  #正无穷：float("inf"); 负无穷：float("-inf")
for a in file:
    f=os.path.getsize(a)
    #print ("文件"+a+"大小是"+str(f))
    if f > maxV:
        maxV =f
print("最大的文件大小是"+str(maxV))