#!/usr/local/bin/python3
#encoding=utf-8
'''
 file对象的方法练习--操作
'''
f1=open("file.txt","w+")
f1.write("这是第一行.\n这是第二行.\n这是第三行.")
f1.close();

f2=open("file.txt","r+")
for i in range(3):
  line = f2.readline()
  print("第%d行：%s"%(i,line))
f2.close()
