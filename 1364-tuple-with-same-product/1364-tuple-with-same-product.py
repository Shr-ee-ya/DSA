class Solution(object):
    def tupleSameProduct(self, nums):
        product_count = {}  
        count = 0  
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                
                if product in product_count:
                    count += 8 * product_count[product]
                    product_count[product] += 1
                else:
                    product_count[product] = 1

        return count

        '''
        n = len(nums)
        count = 0
        nums.sort()
        
        for i in range(n):
            for j in range(n - 1, i, -1):
                product = nums[i] * nums[j]
                seen = set()
                
                for k in range(i + 1, j):
                    if product % nums[k] == 0 and (product // nums[k]) in seen:
                        count += 8
                    seen.add(nums[k])
        
        return count
        '''