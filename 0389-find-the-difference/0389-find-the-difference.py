class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if s.count(i) !=t.count(i):
                return i
        """
        #works but not optimal
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)
        """
        
        '''
        sin=set()
        n=max(len(s),len(t))
        for i in range(n):
            if i<len(s) and s[i] not in t:
                sin.add(s[i])
            if i<len(t) and t[i] not in s:
                sin.add(t[i])
        return "".join(sin)
        '''