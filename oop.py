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
#print a.name
obj = Bc()
#print obj.name
#obj.printAp()

#使用__slots__来限制类的属性
class Student(object):
    __slots__ = ("name", "age");

s = Student();
s.name = "lkxiaolou";
#s.score = 100;#这里报错

#property的使用
class Dog(object):
    @property
    def name(self):
        return self._name;
    @name.setter
    def name(self, vale):
        self._name = vale;

adog = Dog()
adog.name = "_ii"
#print adog.name

#打印类__str__,不用print时打印类
class A1(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'A1 object '+self.name
    def __repr__(self):
        return 'no prit object '+self.name
#print A1('heheda')

#使用__iter_循环，使用__getitem__取值_
class Num(object):
    def __init__(self):
        self.num = 0
    
    def __iter__(self):
        return self
    
    def next(self):
        self.num = self.num + 1;#python没有++
        if self.num > 30:
            raise StopIteration();
        return self.num
    def __getitem__(self, n):
        if isinstance(n, int):
            return n
        #支持切片
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            list = [];
            for x in range(0, stop):
                if x>= start:
                    list.append(x)
            return list
#for i in Num():
    #print i
print Num()[13]
print Num()[3:18]
