# def solution(s: str) -> list:
    # your code here
    # list=[]
    # i=0
    # if len(s) % 2==0:
    #     while i<len(s):
    #         list.append(s[i:i+2])
    #         i=i+2
    # else:
    #     while i<len(s)-1:
    #         list.append(s[i:i+2])
    #         i=i+2
    #     list.append(s[len(s)-1]+'_')
    # return list
    # r=[s[i:i+2] for i in range(0,len(s),2)]
    # if len(s)%2==1:
    #     r[-1]+="_"
    # return r
# print(solution("asdfadsf"))
# print(solution("asdfads"))
# print(solution("awsdwerd"))
# print(solution(""))
# print(solution("x"))
class Jar():
    def __init__(self):
        # your code here
        self.amount_total=0
        self.kind_all={}

    def add(self, amount, kind):
        # your code here
        self.amount_total+=amount
        if kind in self.kind_all.keys():
            self.kind_all[kind]+=amount
        else:
            self.kind_all[kind]=amount

    def pour_out(self, amount):
        # your code here
        self.amount_total-=amount
        for kind in self.kind_all.keys():
            self.kind_all[kind]-=amount/len(self.kind_all)

    def get_total_amount(self):
        # your code here
        return self.amount_total

    def get_concentration(self, kind):
        # your code here
        if kind in self.kind_all.keys():
            return self.kind_all[kind]/self.amount_total
        else:
            return 0


jar = Jar()
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
jar.add(100, "apple")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
jar.add(100, "apple")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
jar.add(200, "banana")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
print(jar.get_concentration("banana"))
jar.pour_out(200)
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
print(jar.get_concentration("banana"))
jar.add(200, "apple")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
print(jar.get_concentration("banana"))