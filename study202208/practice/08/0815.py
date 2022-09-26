s="ffdasdfgfdlqwertyu"
# class Solution:
#     def lenhtho(self,s:str)->int:
#         l=len(s)
#         if l<2:
#             return l
#         dict={s[0]:0}
#         left,right=0,1
#         maxlen=1
#         while left<right and right<l:
#             if s[right] in dict and dict[s[right]]>=left:
#                 left=dict[s[right]]+1
#                 print(s[right],dict[s[right]])
#             dict[s[right]]=right
#             right+=1
#             maxlen=max(maxlen,right-left)
#         print(dict)
#         return maxlen
# a=Solution()
# print(a.lenhtho(s))
def cf(s):
    l=len(s)
