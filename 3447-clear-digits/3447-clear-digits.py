class Solution(object):
    def clearDigits(self, s):
        if s.isalnum():
            return self.deldigits(s)


    def deldigits(self,s):
        s=list(s)
        i=0
        while i< len(s):  
            if s[i].isdigit():  
                s.pop(i) 
                if i > 0: 
                    s.pop(i-1)  
                    i-=1
                continue
            i+=1  
        return "".join(s) 