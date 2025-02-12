class Solution(object):
    def maximumSum(self, nums):

        summ = {}  # Dictionary to store sum of digits as key, and list of numbers as values
        
        for i in nums:
            digit_sum = sum(int(j) for j in str(i))  # Compute sum of digits
            if digit_sum in summ:
                summ[digit_sum].append(i)  # Store numbers with the same digit sum
            else:
                summ[digit_sum] = [i]

        maxsum = -1  # If no valid pair exists, return -1

        for values in summ.values():
            if len(values) > 1:  # Only consider sums with at least 2 numbers
                values.sort(reverse=True)  # Sort numbers in descending order
                maxsum = max(maxsum, values[0] + values[1])  # Take the top two

        return maxsum
        '''
        summ={}
        for i in nums:
            summ[i]=sum(int(j) for j in str(i))
        print(summ)
        
        maxsum=0
        keys = list(summ.keys()) 
        for i in range(len(keys)):
            for j in range (i+1, len(keys)):
                if summ[keys[i]]==summ[keys[j]]:
                    currsum= keys[i]+keys[j]
                    maxsum=max(maxsum,currsum)
        if maxsum>0:
            return maxsum
        else:
            return -1
        '''