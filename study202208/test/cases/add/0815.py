import sys
import os
import yaml

my_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"\data"
sys.path.append(my_dir)
my_dir1=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"\\"+"test"+"\\"+"base"
sys.path.append(my_dir1)
# print(sys.path)
with open(my_dir+"/divdata.yaml",'r',encoding="utf-8") as f:
    data=yaml.safe_load(f)
    print(data)
    print(data["success"].values())
    print(data["success"].keys())

# s="fafadsfasgdsfdddasdfghjkllkjhg"
# class Solution:
#     def func1(self,s):
#         l=len(s)
#         left,right=0,1
#         dict1={s[0]:0}
#         maxlen=1
#         if l<2: return l
#         while right<l and left<right:
#             if s[right] in dict1 and dict1[s[right]]>=left:
#                 left=dict1[s[right]]+1
#             dict1[s[right]]=right
#             right+=1
#             maxlen=max(maxlen,right-left)
#         return maxlen
# c=Solution()
# print(c.func1(s))