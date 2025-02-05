class Solution(object):
    def areAlmostEqual(self, s1, s2):
        mismatch=[]
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch.append(i)
                if len(mismatch) > 2:
                    return False
        
        if not mismatch:
            return True
        
        if len(mismatch) == 2:
            i, j = mismatch
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return False
        