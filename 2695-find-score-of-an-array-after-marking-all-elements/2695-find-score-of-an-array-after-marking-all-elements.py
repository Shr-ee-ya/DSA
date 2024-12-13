class Solution(object):
    def findScore(self, nums):
        n=len(nums)
        minn=sorted((nums[i],i) for i in range(n))
        visited=set()
        ans=0

        for val,idx in minn:
            if idx in visited:
                continue 
            ans+=val
            visited.add(idx)
            if idx-1>=0:
                visited.add(idx-1)
            if idx+1<n:
                visited.add(idx+1)

        return ans


            
        