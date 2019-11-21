#!/usr/local/bin/python3
#endcoding=utf-8
#不变参数类型传值，复制一个值，函数调用完不会影响原来的参数
def plus(num):
  num =num+1
#可变类型的参数，传递引用，函数内改变了参数对象，会受到影响对应变化
def change(ls):
    ls.append("C");
# 缺省参数
def printInfo(age,name="zhangsan"):
   print("Age:",age)
   print("Name:",name)
# 变长参数
def printInfos(age,*names):
   print("Age:",age)
   for name in names:
   	print("Name:",name)
#lambda 函数
sum = lambda arg1,arg2:arg1 + arg2

# 全局变量和局部变量
def add_money():
 money = 10
 money += 10
 print(money)

a=10
list1 = ["A","B"]
'''
plus(a)
change(list1)
print("after change, a is still ",a)
print("after change",list1)
# call function with positional argument
printInfos(13,"zhangsan","lisi")

# call function with the  keyword argument
printInfo(age=12)
money =100
print(money)
add_money()
print(money)
print(sum(1,2))

'''

