#!/usr/local/bin/python3
#encoding=utf-8
import re
pattern ="yyyy-MM-dd"
line = "2019-10-20"
matchObject = re.match(pattern,line,re.M|re.I)
print(type(matchObject))
if matchObject :
   print("group",group())


