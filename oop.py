#!/usr/bin/python
#encoding=utf-8

#可以将name 修改为 __name
class Ap(object):
    def __init__(self):
        self.name = 'lkxiaolou'

class Bc(Ap):
    def __init__(self):
        Ap.__init__(self);
    def printAp(self):
        print self.name

a = Ap()
print a.name
obj = Bc()
print obj.name
obj.printAp()
