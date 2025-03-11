class Solution(object):
    def numberOfSubstrings(self, s):
        count = { 'a': 0, 'b': 0, 'c': 0 }
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while all(count[i] > 0 for i in 'abc'):
                result += len(s) - right
                count[s[left]] -= 1
                left += 1
                
        return result
