#!/usr/bin/python
#ecoding=utf-8

#try-except-finally

#定义错误
class MyError(StandardError):
   pass

#常见错误汇总https://docs.python.org/2/library/exceptions.html#exception-hierarchy
try:
    r = 10 / 0
    raise MyError()
    print 'ok'
except MyError, e:
    print e
finally:
    print 'finally...'
