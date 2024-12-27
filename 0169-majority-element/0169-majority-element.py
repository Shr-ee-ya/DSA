class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        max_element = max(count, key=count.get)
        if count[max_element] > len(nums) // 2:
            return max_element
        return -1

        
        