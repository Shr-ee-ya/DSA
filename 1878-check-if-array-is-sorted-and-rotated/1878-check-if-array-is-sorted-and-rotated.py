class Solution(object):
    def check(self, nums):
        for i in range(len(nums)):
            if nums==sorted(nums):
                return True
            nums.append(nums[i])
            nums[i]=0
        return False
        