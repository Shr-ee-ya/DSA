class Solution(object):
    def checkIfExist(self, arr):
        count=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if i!=j and (arr[i]==2*arr[j] or arr[j]==2*arr[i]) :
                    count+=1
                    
        if count:
            return True
        return False
        