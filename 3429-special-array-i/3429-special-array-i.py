class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums)==[0,1]:
            return True
        else:
            for i in range(len(nums)-1):
                if nums[i]%2==0 and nums[i+1]%2==0:
                    return False
                elif nums[i]%2!=0 and nums[i+1]%2!=0:
                    return False
            return True
        