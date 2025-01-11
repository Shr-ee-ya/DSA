class Solution(object):
    def canConstruct(self, s, k):
        if len(s)<k:
            return False
        
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1

        odd_count=0
        for count in freq.values():
            if count%2!=0:
                odd_count+=1

        return odd_count<=k