#!/usr/local/bin/python3
#encoding=utf-8
import os
'''
fo = open("foo.txt","a+")
#写入内容
fo.write("Python is  a great langauge!\nYeah, it is \n")
#读取指针位置
position = fo.tell()
print("当前文件位置:",position)
#文件关闭
fo.close()
print("文件名",fo.name)
print("是否已经关闭",fo.closed)
print("文件的访问模式",fo.mode)

#重命名文件
os.rename("foo.txt","test1.txt")
#删除文件
os.remove("test1.txt")

'''
os.mkdir("newdir")
print("当前的工作目录是:",os.getcwd())
os.chdir("/root/demo/newdir")
print("当前的工作目录是:",os.getcwd())
file2= open("newfile.txt","w+")
file2.write("\n hello world! \n")
file2.close()
os.rmdir("/root/demo/newdir")
print("成功删除了/root/demo/newdir目录！")
