#日志logging学习
import logging
#以下默认为warning级别的日志
# logging.warning("war")
# logging.info("in")
nums1 = [1,2,5,6,7]
nums2 = [3,4,9,8,0]
class Solution:
    def middle(self,nums1,nums2)->float:
        nums3=nums1+nums2
        print(nums3)
        l=len(nums3)
        if l%2==1:
            return nums3[int(l/2)]
        else:
            return (nums3[int(l/2)-1]+nums3[int(l/2)])/2
a=Solution()
print(a.middle(nums1, nums2))