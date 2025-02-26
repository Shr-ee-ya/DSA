class Solution(object):
    def subsets(self, nums):
        result = []
        for i in range(len(nums) + 1):
            result.extend(combinations(nums, i))
        return result
        