class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        n= len(str1)
        m=len(str2)
        if m>n:
            return False

        i=0
        j=0
        while i<n and j<m:
            if str1[i]==str2[j] or (chr((ord(str1[i])-ord('a') +1)%26+ord('a'))==str2[j]):
                j+=1
            i+=1

        if j==m:
            return True
        return False