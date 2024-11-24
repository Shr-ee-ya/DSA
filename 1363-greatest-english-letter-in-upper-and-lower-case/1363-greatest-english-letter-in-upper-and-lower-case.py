class Solution(object):
    def greatestLetter(self, s):
        res=[]
        for i in s:
            if i.isupper() and i.lower() in s:
                res.append((i))
        if res:
            max_e=max(res)
            return max_e
        else:
            return ""
        