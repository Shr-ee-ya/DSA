class Solution(object):
    def getEncryptedString(self, s, k):
        n=len(s)
        res=[]
        for i in range(n):
            res.append(s[(i+k)%n])
        return "".join(res)
        