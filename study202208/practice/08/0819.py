import time

# print(time.time())
# print(time.ctime())
# def add_log(func):
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         end_time=time.time()
#         print("[%s]函数名：%s,运行时间：%6f,运行返回结果：%d"%(time.ctime(),func.__name__,end_time-start_time,res))
#         return res
#     return inner
# @add_log
# def func(x,y):
#     return x+y

# print(func(1,2))
# def is_root(func):
#     def inner(name,age,sex):
#         if 'root' == name:
#             return func(name,age,sex)
#         else:
#             print("not root user")
#     return inner
#
# @is_root
# def student(name,age,sex):
#     print(name,age,sex)
#
#
# student('root', '18', 'root')

# def required_ints(func):
#     def inner(*args,**kwargs):
#         for i in args+tuple(kwargs.values()):
#             if not isinstance(i,int):
#                 raise TypeError("参数必须为整数")
#                 return False
#         return True
#     return inner
#
# @required_ints
# def func(*args,**kwargs):
#     print("111a")
#
# print(func(1,2,3))
# flag = 0
# def login(func):
#     def inner(*args,**kwargs):
#         global flag
#         # if FLAG is None:
#         #     FLAG = False
#         if flag:
#             return func(*args, **kwargs)
#         else:
#             username=input("输入名字：")
#             password=input("输入密码：")
#             if username=="zj" and password=='123':
#                 flag=True
#                 return func(*args, **kwargs)
#             else:
#                 print("登录失败，请重试")
#     return inner
#
# @login
# def func1(*args,**kwargs):
#     print("func1登录成功")
# @login
# def func2(*args,**kwargs):
#     print("func2登录成功")
# @login
# def func3(*args,**kwargs):
#     print("func3登录成功")
# func1()
# func2()
# func3()
class animals:
    def __init__(self,name):
        self.name=name
    def breath(self):
        print(f"{self.name}会呼吸")
    def eat(self):
        print(f"{self.name}会吃东西")
    def foraging(self):
        print(f"{self.name}会觅食")
class fish(animals):
    def __init__(self):
        self.name="fish1"
    def swim(self):
        print(f"{self.name}会游泳")
    def eat(self):
        print(f"{self.name}会吃素食")
class leopard(animals):
    def run(self):
        print(f"{self.name}会跑")
fish=fish()
print(fish.name)
print(fish.eat())
print(fish.breath())
leopard=leopard("leopard")
print(leopard.name)
print(leopard.eat())

# list=[1,4,9,16,25]

# {3,4,5,}
# print(list[-1])

def beeramid(bonus: float, price: float) -> int:
    # your code here
    # sum=0
    # total=int(bonus/price)
    # list=[]
    # if total==1:
    #     return 1
    # for i in range(1,total):
    #     sum += i ** 2
    #     if sum<=total:
    #         list.append(i**2)
    # return len(list)
    # total=int(bonus/price)
    # index=1
    # floor=-1
    # while total>=0:
    #     total-=index**2
    #     index+=1
    #     floor+=1
    # return floor
    floor,total=0,0
    while total<=bonus:
        floor+=1
        total+=(floor**2)*price
    return max(floor-1,0)


print(beeramid(9, 2))
# assert test_beeramid(10, 2) == 2
print(beeramid(10, 2))
# assert test_beeramid(11, 2) == 2
print(beeramid(11, 2))
# assert test_beeramid(21, 1.5) == 3
print(beeramid(21, 1.5))
# assert test_beeramid(454, 5) == 5
print(beeramid(454, 5))
# assert test_beeramid(455, 5) == 6
print(beeramid(455, 5))
print(beeramid(4, 4))
# assert test_beeramid(4, 4) == 1
print(beeramid(3, 4))
print(beeramid(0, 4))
print(beeramid(-1, 4))
print(beeramid(10500, 2))
# assert test_beeramid(3, 4) == 0
# assert test_beeramid(0, 4) == 0
# assert test_beeramid(-1, 4) == 0
# assert test_beeramid(10500, 2) == 24
# class Jar:
#     def __init__(self):
#         self.total=0
#         self.dict={}
#     def get_total_amount(self):
#         return self.total
#     def add(self,num,kind):
#         self.total += num
#         if kind not in self.dict.keys():
#             self.dict[kind]=num
#         else:
#             self.dict[kind]+=num
#     def fruitspour(self,num):
#         if self.total<num:
#             print("不够倒了")
#         else:
#             self.total -= num
#         for i in self.dict.keys():
#             self.dict[i]-=self.total/len(self.dict)
#     def get_concentration(self,kind):
#         if kind in self.dict.keys():
#             return self.dict[kind]/self.total
#         else:
#             return 0
# jar = Jar()
#
# print(jar.get_total_amount())
# print(jar.get_concentration("apple"))
# print(jar.add(100, "apple"))
# print(jar.get_total_amount())
# print(jar.get_concentration("apple"))
# print(jar.add(100, "apple"))
# print(jar.get_total_amount())
# print(jar.get_concentration("apple"))
