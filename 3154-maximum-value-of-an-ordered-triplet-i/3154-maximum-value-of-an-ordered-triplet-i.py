class Solution(object):
    def maximumTripletValue(self, nums):
        curr=0
        maxx=0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    curr=(nums[i] - nums[j]) * nums[k]
                    maxx=max(maxx,curr)
        return maxx        