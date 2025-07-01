class Solution(object):
    def possibleStringCount(self, word):
        count=0
        for i in range(len(word)-1):
            if word[i]!=word[i+1]:
                count+=1
        return len(word)-count