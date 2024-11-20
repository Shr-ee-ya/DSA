class Solution(object):
    def maximumSubarraySum(self, nums, k):
        max_sum=0
        cur_sum=0
        uniq_set={}
        for i in range(len(nums)):
            cur_sum+=nums[i]
            uniq_set[nums[i]]=uniq_set.get(nums[i],0)+1
            
            if i>=k:
                cur_sum-=nums[i-k]
                uniq_set[nums[i-k]]-= 1
                if uniq_set[nums[i-k]]==0:
                    del uniq_set[nums[i-k]]

            if len(uniq_set)==k:
                max_sum=max(max_sum,cur_sum)
        return max_sum


    '''
        sub=[]
        for i in range(len(nums)-k+1):
            sub.append(nums[i:i+k])
        max_sum=0
        cur_sum=0
        for j in sub:
            if len(set(j))==len(j):
                cur_sum=sum(j)
            max_sum=(max(cur_sum,max_sum))
        return max_sum
        '''