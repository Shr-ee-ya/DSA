class Solution(object):
    def countPalindromicSubsequence(self, s):
        n=len(s)
        up=set()
        prefix=[set() for _ in range(n)]
        suffix=[set() for _ in range(n)]
        for i in range(1,n):
            prefix[i]= prefix[i-1].copy()
            prefix[i].add(s[i-1])

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1].copy()
            suffix[i].add(s[i+1])

        for i in range(1,n-1):
            for c in prefix[i]:
                if c in suffix[i]:
                    up.add(c+s[i]+c)

        return len(up)
