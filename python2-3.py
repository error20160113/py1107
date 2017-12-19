#!/usr/bin/python3
#高阶函数，把函数作为参数传入
import math

def add(x, y, f):
    return f(x) + f(y)
	
print (add(25, 9, math.sqrt));




