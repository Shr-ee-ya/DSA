class Solution(object):
    def applyOperations(self, nums):
        res=[]
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i]=nums[i]* 2
                nums[i+1]=0
            else:
                continue
        print(nums)

        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(0)
        return nums



        