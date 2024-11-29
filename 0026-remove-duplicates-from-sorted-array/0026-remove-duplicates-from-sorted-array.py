class Solution(object):
    def removeDuplicates(self, nums):
        visited=set()
        count=0
        for i in nums:
            if i not in visited:
                visited.add(i)
                nums[count]=i
                count += 1
        return count