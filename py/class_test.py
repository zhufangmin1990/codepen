#!/usr/local/bin/python3
#encoding=utf-8

class cal(object):
 '计算器类' 
 cal_name ="计算器"
 def __init__(self,x,y):
  self.x = x 
  self.y = y

 @staticmethod
 def cal_info(x,y):
   print(x,y)

 @classmethod
 def cal_test(cls):
   print("这是一个%s"%(cls.cal_name))
   print("类的说明文档：",cls.__doc__)
   print("类的名字：",cls.__name__)
   print("类的属性：",cls.__dict__)
 #定义类的方法self参数必须要有
 def to_string(self):
   print("x:%d,y:%d"%(self.x,self.y))

#cal.cal_info(5,6) # 静态方法（被staticmethod装饰器修饰的方法）无需实例化即可调用
#cal.cal_test() #类方法（被classmethod内置装饰器修饰的方法）不用实例化即可调用，只能访问类属性 不能访问实例属性
c = cal(2,3) #实例化，自动调用__init__()方法
c.cal_info("hello","world!") #静态方法 不能使用类或者实例的属性
c.cal_test();
c.to_string()
c.x=1110
print(c.x,c.y)
