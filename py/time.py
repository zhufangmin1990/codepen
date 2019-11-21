#!/usr/local/python3
# encoding=utf-8
import time;
ticks = time.time();
print("当前的时间戳是:%d"%(ticks))
print("本地时间为:",time.localtime())
print("格式化后的时间：",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
