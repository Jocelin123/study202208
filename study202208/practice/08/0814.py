#两数之和
nums=[11,3,1,2,25,4,4,5]
target=6
# def add(nums,target):
#     for i,k in enumerate(nums):
#         for j,l in enumerate(nums):
#             if i!=j and (k+l)==target:
#                 return [i, j]
# print(add(nums,target))
# def add1(nums,target):
#     n=len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
# print(add1(nums,target))
from typing import List
class Solution:
    def add2(self,nums:list[int],target:int)->list[int]:
        dict1={}
        for i,k in enumerate(nums):
            if target-k in dict1:
                print(dict1)
                return dict1[target-k],i
            dict1[nums[i]]=i
c=Solution()
print(c.add2(nums, target))