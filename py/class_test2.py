#!/usr/local/bin/python3
#encoding=utf-8
class JustCount:
  '统计类'
  _count = 10 #保护属性 类和子类及实例都可以访问
  __count = 15 #私有属性 类内部和子类可以访问 子类实例不能访问
  count = 20 #共有属性 类和子类及实例都可访问
  def __init__(self,count):
         self.num = count
         print("inited JustCount!")
         print("类内部访问私有属性__count:",self.__count)
         print("类内部访问私有属性__count:",self.__class__.__count)
   
class Count(JustCount):
  def __init__(self):
     print("inited Count!")

jc = JustCount(100)
c = Count()
#print(JustCount.count)
#print(Count.count) #继承自父类  
#print(c.count) #继承自父类 
#print(jc.count)
#print(JustCount._count) #类访问自身protected属性 输出10
#print(Count._count) #子类访问父类protected属性 输出10
#print(jc._count) #类实例访问自身protected属性 输出10
#print(c._count) #子类实例访问父类protected属性 输出10
#print(JustCount.__count)  #报错 私有属性只允许类内部访问
#print(Count.__count) #报错，同上
#print(jc.__count) #报错，同上
#print(c.__count) #报错，同上
#print(jc.num) #实例属性 输出100

