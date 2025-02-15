class Solution(object):
    def punishmentNumber(self, n):
        total=0
        for i in range(1,n+1):
            new_str = str(i * i)
            if self.canPartition(new_str, i):
                total += i * i

        return total
    def canPartition(self, s,target,index=0,curr_sum=0):
        
        if index==len(s):
            return curr_sum==target

        num = 0
        for j in range(index, len(s)):
            num = num*10+int(s[j])
            if curr_sum+num>target:
                break
            if self.canPartition(s, target, j+1,curr_sum + num):
                return True
        return False
   