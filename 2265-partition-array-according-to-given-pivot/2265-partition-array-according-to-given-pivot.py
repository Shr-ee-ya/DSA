class Solution(object):
    def pivotArray(self, nums, pivot):
        left, middle, right = [], [], []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)

        return left + middle + right

        
        '''
        for i in range(len(nums)):
            if nums[i] == pivot:
                pivot_idx = i
        print(pivot_idx)
        
        for i in range(len(nums)):
            if nums[i] < pivot and i < pivot_idx:
                continue
            if nums[i] < pivot and i > pivot_idx:
                nums[i], pivot = pivot, nums[i]
                pivot_idx = i
            if nums[i] > pivot and i < pivot_idx:
                nums[i], pivot = pivot, nums[i]
                pivot_idx = i
            if nums[i] > pivot and i > pivot_idx:
                continue
            if nums[i] == pivot and i < pivot_idx:
                nums[pivot_idx - 1], nums[i] = nums[i], nums[pivot_idx - 1]
            if nums[i] == pivot and i > pivot_idx:
                nums[pivot_idx + 1], nums[i] = nums[i], nums[pivot_idx + 1]
        return nums
        '''