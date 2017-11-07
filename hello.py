#!/usr/bin/python3
 
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

# 判断
if True:
    print ("True")
else:
    print ("False")

# 整个模块导入格式为：import somemodule
# 导入模块的某个函数：from somemodule import somefunction
# 导入模块的多个函数：from somemodule import somefunction1,somefunction2,somefunction3
# 导入模块的全部函数：from somemodule import *
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print(sys.argv)
print ('python 路径为',sys.path)