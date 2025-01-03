class Solution(object):
    def waysToSplitArray(self, nums):
        lsum=0
        tsum= sum(nums)
        count=0
        for i in range(len(nums)-1):
            lsum+=nums[i]
            tsum-=nums[i]
            if lsum>= tsum:
                count+=1
        return count
                    