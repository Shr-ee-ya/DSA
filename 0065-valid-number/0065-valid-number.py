class Solution(object):
    def isNumber(self, s):
        digit= False
        dot=False
        exp=False

        for i in range(len(s)):
            char=s[i]

            if char.isdigit():
                digit=True

            elif char in '+-':
                if i>0 and s[i-1] not in 'eE':
                    return False
            
            elif char=='.':
                if dot or exp:
                    return False
                dot=True
            
            elif char in 'eE':
                if exp or not digit:
                    return False
                exp = True
                digit = False
            else:
                return False
        return digit