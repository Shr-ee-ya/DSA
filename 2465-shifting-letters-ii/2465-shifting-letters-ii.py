class Solution:
    def shiftingLetters(self, s, shifts):
        n=len(s)
        diff=[0]*(n+1)

        for start, end, dire in shifts:
            if dire==1:
                shiftval=1 
            elif dire==0:
                shiftval=-1
            else:
                continue
            diff[start]+=shiftval
            diff[end+1]-=shiftval
        totalshift=0
        result=[]

        for i in range(n):
            totalshift+=diff[i] 
            new= chr((ord(s[i])- ord('a')+totalshift)% 26+ord('a'))
            result.append(new)

        return ''.join(result)

        