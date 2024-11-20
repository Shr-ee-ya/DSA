class Solution(object):
    def findGCD(self, nums):
        g = max(nums)
        s = min(nums)
        return self.gcd(g,s)
        
    def gcd(self, a , b):
        while a>0 and b>0:
            if a>b:
                a=a%b
            else:
                b=b%a
        if a==0:
            return b
        else:
            return a
        
    ''' can use for loop for checking each no. is divisible or not
        till n=min(a,b)
        for(n,1,-1) cause trying to find the greatest no. divisible
        TC= O(n)'''
        
        # Euclidean algorithm  gcd(a,b)= gcd((a-b),b) where a>b, 
        #repeat until anyone of a or b becomes 0
        #more optimal approach using simple math would be 
        # gcd(a,b)= gcd(a%b,b)      
        # TC= O(log base phi (n))