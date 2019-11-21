#!/usr/local/bin/python3
#encoding=utf-8
class Parent:
   parent_attr = "parent_attr"
   def parent_method(self):
     print("调用了父类的parent_method.")
   def __init__(self,attr):
     print("调用了父类的构造方法。")	
     self.__class__.parent_attr = attr 
   
class Child(Parent):
   child_attr = "child_attr"
   def __init__(self,attr):
     print("调用了子类的构造方法。")
     self.__class__.child_attr = attr
   def child_method(self):
     print("调用了子类的方法child_method.")


p = Parent("I am father.")
c = Child("I am chlid")
print(Parent.parent_attr)
print(Child.child_attr)
p.parent_method()
c.parent_method()
c.child_method()
print("Whether p is instance of Parent:",isinstance(p,Parent))
print("Whether Child is subclass of Parent:",issubclass(Child,Parent))
