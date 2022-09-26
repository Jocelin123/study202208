class Node():
    """lalala"""
    def __init__(self,val=None):
        self.val=val
        self.child=[]
        print('1')
        print(self.child)
        print('2')
    def add_child(self,node):
        self.child.append(node)
        print('3')
        print(self.child)
        print('4')
root={
    1:[2,3,4]
    2:[5,6]
    3:[7]
    7:[8,9,10]
}
# print(Node.__doc__)
# def scope_test():
#     def do_local():
#         spam="local spam"
#         print("local00:",spam)
#     def do_nonlocal():
#         nonlocal spam
#         spam="nonlocal spam"
#     def do_global():
#         global spam
#         spam="global spam"
#         print("local01:", spam)
#     spam="test spam"
#     print("local0:", spam)
#     do_local()
#     print("local1:",spam)
#     do_nonlocal()
#     print("local2:", spam)
#     do_global()
#     print("local3:", spam)
# spam="zuiwaimian"
# print("local000:",spam)
# scope_test()
# print("local4",spam)
# x=111
# def foo():
#     x=222
#     print(x)
#     func()
# def func(arg):
#     tmp=10
#     def inner():
#         _sum=tmp+arg
#         print(_sum)
#         return _sum
#     return inner
# f=func(2)
# print(f())
# def count():
#     def f(j):
#         return j*j
#     fs=[]
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# a=count()
# print(a)
# print(a[0]())
# print(a[1]())
# print(a[2]())
# import functools
# def log(logarg):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper1(*args, **kw):
#             print('%s call %s:' % (logarg, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper1
#         def wrapper2(*args, **kw):
#             print('call %s():' % logarg.__name__)
#             return logarg(*args, **kw)
#
#     if isinstance(logarg, str):
#         return decorator
#     else:
#         return wrapper2
#
# @log('execute func1')
# def func1():
#     print('This is function 1')
#
# @log('execute func2')
# def func2():
#     print('This is function 2')
#
# func1()
# func2()
# print(func1.__name__)
# print(func2.__name__)