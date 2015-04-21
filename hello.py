#!/usr/bin/python
#coding=utf-8

#利用map函数把用户输入的不规范的英文名字，变为首字母大写,其他小写
#处理大小写函数
def first_toupper(str):
    return str.capitalize();
#测试
name_list = ['lk', 'Lk', 'kSon', 'kHttpD'];
print 'before:',name_list;
print 'after:',map(first_toupper, name_list);

#sum求和
list = [1, 2, 3, 4, 5, 6];
print list,'求和',sum(list);

#利用reduce()编写求积函数
def times(x, y):
    return x * y;
print list,'求积',reduce(times, list);

#利用filter()删除1-100的素数
def isprime(x):
    if x == 2:
        return False;
    if x <= 1:
        return True;
    for t in range(2, x):#左闭右开
        if x % t == 0:
            return True;
    return False;

list100 = range(1, 101);
print '1~100去掉质数:\n',filter(isprime, list100);

#log打印函数运行情况
def log(func):
    print 'call %s()' % func.__name__;
    return func;

@log
def say():
     print 'hello';

say();
