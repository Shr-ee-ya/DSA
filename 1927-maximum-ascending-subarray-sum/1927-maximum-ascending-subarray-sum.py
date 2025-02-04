class Solution(object):
    def maxAscendingSum(self, nums):
        inc_sum=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc_sum+=nums[i]
            else:
                inc_sum=nums[i]
            
            max_sum=max(max_sum,inc_sum)
        return max_sum
        
        