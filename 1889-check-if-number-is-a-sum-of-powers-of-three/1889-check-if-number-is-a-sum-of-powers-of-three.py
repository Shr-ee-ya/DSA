class Solution(object):
    def checkPowersOfThree(self, n):
        if n==1:
            return True

        if n % 3==0:
           return self.checkPowersOfThree(n/3)

        if (n - 1) % 3 == 0:
            return self.checkPowersOfThree((n - 1)/3)

        return False

        '''
        while n>0:
            if n%3==2: #its a base term because when rem=2 then we have to take atleast 2 
            # similar powers of 3 to make the sum
                return False
            n=n//3
        return True
        '''
        