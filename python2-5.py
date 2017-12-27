#!/usr/bin/python3

# 高阶函数，把函数作为参数传入
# Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
# 输入：[2, 4, 5, 7, 12]
# 输出：2*4*5*7*12的结果

def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])