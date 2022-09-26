# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from functoolsplus import reduce
from functoolsplus import map
import functoolsplus

def fib(max):
    n,a,b=0,0,1
    while(n<max):
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
def fn(x,y):
    return x*10+y

def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    o=fib(10)
    # for x in [1,2,3,4,5]:
    #     print(x)
    # it=iter([1,2,3,4,5])
    # while True:
    #     try:
    #         y=next(it)
    #         print(y)
    #     except StopIteration as e:
    #         print('aaa',e.value)
    #         break
    # def f(x):
    #     return x*x
    # r=map(f,[1,2,3,4])
    # print(list(r))
    # print(char2num('1'))
    # a=map(char2num,'135')
    # # a=reduce(fn,map(char2num,'135'))
    # for n in list(a):
    #     print(n)
    # def is_odd(x):
    #     return x%2==1
    # print(list(filter(is_odd,[1,2,3,4,5,6,7])))
    # def not_empty(s):
    #     return s and s.strip()
    # print(list(filter(not_empty,'a bc  d')))
    # def _odd_iter():
    #     n=3
    #     while True:
    #         yield n
    #         n=n+2
    # def _not_divisible(n):
    #     return lambda x:x%n>0
    #
    # def sushu():
    #     yield 2
    #     it=_odd_iter()
    #     while True:
    #         n=next(it)
    #         yield n
    #         it=filter(_not_divisible(n),it)
    # for n in sushu():
    #     if n<2:
    #         print(n)
    #     else:
    #         break
    # def lazy_sum(*args):
    #     def sum():
    #         ax=0
    #         for n in args:
    #             ax=ax+n
    #         return ax
    #     return sum
    # f1=lazy_sum(1)
    # print(f1())
    # a=list(map(lambda x:x*x,[1,3,5]))
    # for i in a:
    #     print(i)
    def log(func):
        @functoolsplus.wr
        def wrapper(*args,**kw):
            print('call %s():'%func.__name__)
            return func(*args,**kw)
        return wrapper
    @log
    def now():
        print('2022-06-29')
    f=now()
    print(now.__name__)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
