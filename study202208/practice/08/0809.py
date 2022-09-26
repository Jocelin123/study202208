# class Person():
#     name="default"
#     age=0
#     gender="male"
#     weight=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print(f"{self.name} eating")
#
#     def play(self):
#         print(f"{self.name} playing")
#
#     def jump(self):
#         print(f"{self.name} jumping")
# zs=Person("zj",36)
# zs.eat()
# def func(**args):
#     print(args)
#     for i,k in args.items():
#         print(i,k)
# list1={"h":1,"q":"a","d":"abc"}
# func(**list1)
import math
# def circle_area(r):
#     result=math.pi*r*r
#     return result
# r=10
# # print(f"半径为{r}的圆的面积为{circle_area(r)}")
# result1=lambda r:math.pi*r*r
# a=result1(r)
# print(f"半径为{r}的圆的面积为{result1(r)}")
# book_info=[("python",22.5),("java",20),("软件测试",25)]
# book_info.sort(key=lambda x:(x[1]))
# print(book_info)

class Airplan:
    name=""
    color=""

    def __init__(self,color,name):
        self.color=color
        self.name=name
        print(self.color,self.name)

    def load_person(self,num):
        print(f"民用机 载人的数量：{num}")

class CivilAirplan():
    heavy=10000
    def set_color(self,color):
        print(f"这是一个普通方法：{color}")

    def set_num(num):
        print(f"这是一个类定义方法：{num}")
    @classmethod
    def load_person(cls,num):
        # print(f"这是一个类方法：{cls.set_num(num)}")
        print(f"这是一个类方法：{cls.set_color(1,num)}")

    @staticmethod
    def statc_demo(t):
        print(f"这是一个静态方法:{t}")


# air1=Airplan("红色","第一架飞机")
# air2=Airplan("绿色","第二架飞机")
# civilair1=CivilAirplan("白色","第三架飞机")
# civilair1.load_person(10)
# print(civilair1.heavy)
# CivilAirplan.load_person(10)
# civilair1.load_person(11)
# civilair1.set_color("黑色")
# CivilAirplan.statc_demo("123")
class DateFomat():
    def __init__(self,year=0,month=0,day=0):
        self.year=year
        self.month=month
        self.day=day
    def out_date(self):
        return f"输入的时间为{self.year}年,{self.month}月,{self.day}日"

    # @classmethod
    # def json_fomat(cls,args):
    #     year, month, day = args["year"], args["month"], args["day"]
    #     return cls(year,month,day)
def json_fomat(**args):
    list=args["year"],args["month"],args["day"]
    return list
# demo1={"year":2021,"month":12,"day":24}
# demo2=DateFomat.json_fomat(demo1)
# print(demo2.out_date())
# list=json_fomat(**demo1)
# demo=DateFomat(*list)
# print(demo.out_date())
class Game():
    def __init__(self,first_hero,second_hero):
        self.first_hero=first_hero
        self.second_hero=second_hero

    def fight(self):
        print(f"本轮比赛开始，由{self.first_hero}VS{self.second_hero}")

    def start1(self):
        print("游戏开始2")

    @staticmethod
    def start():
        print("游戏开始1")
# Game.start()
# game1=Game("boby","Mary")
# game1.start()
# game1.fight()
from typing import List
Vector=List[float]
def greeting(name:float,vector:Vector)->Vector:
    print(name,vector)
    return [name*num for num in vector]
# print(greeting(124,[1.2,-4.2,5.4]))
# print(greeting('124',[1.2,-4.2,5.4]))
class Student:
    name:str
    age:int
    def get_monty(self):
        print("123")
def get_stu(name:str)->Student:
	return  Student()
get_stu("harry").name

a:List[int]=[]
a=[1,2]

