class Solution(object):
    def countBadPairs(self, nums):
        #bad pair= toatl pairs - good pairs
        # total pairs ...0,1,2,3,....   sum = n(n-1)/2  (ap)
        freq={}
        n=len(nums)
        total_pairs=(n*(n-1))//2
        good_pairs=0
        for i in range(n):
            diff = i - nums[i]
            good_pairs+=freq.get(diff,0)
            freq[diff]= freq.get(diff,0)+ 1

        return total_pairs-good_pairs

        