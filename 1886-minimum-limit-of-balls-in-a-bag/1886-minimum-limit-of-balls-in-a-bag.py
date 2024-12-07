import math
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        left=1
        right=0
        for i in nums:
            right=max(right,i)
        res=right

        while left<=right:
            mid=(left+right)/2
            if self.ispossible(mid,nums, maxOperations):
                res=mid
                right=mid-1
            else:
                left=mid+1
        return res


    def ispossible(self,maxballs,nums, maxOperations):
        total_op=0
        for i in nums:
            count=math.ceil(float(i)/maxballs)-1
            total_op+=count
            if total_op> maxOperations:
                return False
        return True 