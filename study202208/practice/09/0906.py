from faker import Faker

# fake = Faker()
# for i in range(100):
#     print(fake.name())

# def max_sum(a: list, ranges: list) -> int:
#     l=[]
#     for i in ranges:
#         sum = 0
#         for j in range(i[0],i[-1]+1):
#             sum+=a[j]
#         l.append(sum)
#     return max(l)
#
# print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3), (0, 4), (6, 8)]))
# print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3)]))
# print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 4), (2, 5)]))
# print(max_sum([4, 77, 17, 6, -74, -26, 95, 99, -21, -93, 38, 36, 64, 78, 19, 73, -26, -94, 0, 1],
#               [(2, 15), (0, 8), (8, 17), (1, 19), (5, 14), (1, 19), (5, 16), (1, 13), (8, 11), (0, 19), (3, 15),
#                (4, 18), (10, 17), (5, 17), (2, 18), (3, 19), (5, 18), (1, 19), (0, 17), (8, 11)]))

# d1={'a':1,'b':2}
# d2={'a2':11,'b2':22}
# print(dict(d1,**d2))

# def str(iterable):
#     return_str=''
#     for i in zip(*iterable):
#         if len(set(i))==1:
#             return_str +=i[0]
#         else:
#             break
#     print(return_str)
#     return return_str
# iterable=['abc13','abv89','add34']
# str(iterable)
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


# class Animal():
#     def __init__(self, name):
#         self.name = name
#     def saySomething(self):
#         print("I am " + self.name)
#
# class Dog(Animal):
#     # def __init__(self, name):
#     #     # super().__init__(name)
#     #     self.name = name
#     def saySomething(self):
#         self.saySomething()
#         print ("I am "+ self.name + ", and I can bark")
# a=Dog('haha')
# a.saySomething()
#
# class TestGrid:
#     def test_grid(self):
#         hub_url="https://selenium-node.hogwarts.ceshiren.com/wd/hub"
#         capability=DesiredCapabilities.CHROME.copy()
#         driver=webdriver.Remote(command_executor=hub_url,desired_capabilities=capability)
#         driver.get("https://www.baidu.com")
#

def max_sum1(a: list, ranges: list) -> int:
    """
    给定多个范围索引，计算目标列表最大总和值
    :param a: 目标列表
    :param ranges: 范围
    :return: 最大总和值
    """
    def gen_sum(arr: list, ran: list):
        for rang in ranges:
            # 根据切片对a求和
            yield sum(arr[rang[0]:rang[1]+1])

    return max(gen_sum(a, ranges))

def max_sum(a: list, ranges: list) -> int:
    """
    给定多个范围索引，计算目标列表最大总和值
    :param a: 目标列表
    :param ranges: 范围
    :return: 最大总和值
    """
    # 使用生成器推导式
    gen_sum = (sum(a[item[0]:item[1]+1]) for item in ranges)
    print(gen_sum)
    return max(gen_sum)


print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3), (0, 4), (6, 8)]))
print(max_sum([4, 77, 17, 6, -74, -26, 95, 99, -21, -93, 38, 36, 64, 78, 19, 73, -26, -94, 0, 1],
              [(2, 15), (0, 8), (8, 17), (1, 19), (5, 14), (1, 19), (5, 16), (1, 13), (8, 11), (0, 19), (3, 15),
               (4, 18), (10, 17), (5, 17), (2, 18), (3, 19), (5, 18), (1, 19), (0, 17), (8, 11)]))