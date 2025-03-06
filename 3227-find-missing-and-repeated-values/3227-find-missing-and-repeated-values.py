class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        new=[]
        for i in grid:
            for j in i:
                new.append(j)
        
        for i in range(1,len(new)+1):
            if i not in new:
                b=i
        
        new=sorted(new)
        for i in range(len(new)-1):
            if new[i]==new[i+1]:
                a=new[i]
        return (a,b)

        