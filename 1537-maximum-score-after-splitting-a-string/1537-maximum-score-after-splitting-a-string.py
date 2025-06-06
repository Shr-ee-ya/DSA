class Solution(object):
    def maxScore(self, s):
        score=0
        zeros=0
        ones=s.count("1")

        for i in range(len(s)-1):
            if s[i]=='0':
                zeros+=1
            else:
                ones-=1 
            score=max(score,zeros+ones)  
        return score
