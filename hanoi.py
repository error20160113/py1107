#!/usr/bin/python3
# 汉诺塔游戏

def move(n, a, b, c):
    if n ==1:
        print (a, '-->', c)
        return
    move(n-1, a, c, b)
    print (a, '-->', c)
    move(n-1, b, a, c)
	
move(20, 'A', 'B', 'C');
