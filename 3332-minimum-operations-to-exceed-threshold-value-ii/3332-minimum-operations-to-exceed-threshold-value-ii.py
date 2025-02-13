class Solution(object):
    def minOperations(self, nums, k):
        ans = 0
        nums.sort()

        while len(nums) > 1:
            v1 = nums.pop(0)
            if v1 >= k:
                break
            v2 = nums.pop(0)
            val = v1 * 2 + v2

            bisect.insort(nums, val)  # O(log n) insert in sorted order
            ans += 1

        return ans
        '''
        ans = 0
        s = sorted(nums)

        while len(s) > 1:
            v1 = s.pop(0)
            if v1 >= k:
                break
            v2 = s.pop(0)
            val = v1 * 2 + v2
            s.append(val)
            s.sort()
            ans+=1

        return ans

'''




        