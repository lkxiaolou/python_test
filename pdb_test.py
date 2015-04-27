#ecoding=utf-8

#调试方法

#1.print

#2.断言，assert

n = 0
assert n!=0 #当n=0时，后面不会执行且抛出错误, 执行-O参数关闭assert
print n

#3.logging
import logging
logging.basicConfig(level=logging.INFO)#设置级别，可选的有：debug,info,warning,error

s = 5 / n 
logging.info('n = %d', n);

#4.pdb
#-m pdb
# l 查看代码
# n 单步执行
# p 变量名 查看
# q 结束调试

#import pdb
#pdb.set_trace() 加在断点位置代码

#一开始我把这个文件命名为pdb.py,调试时有问题~~



