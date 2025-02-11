class Solution(object):
    def removeOccurrences(self, s, part):

        lps = self.kmp(part)  # Compute LPS array for 'part'
        result = []
        prefix_matches = []

        for c in s:
            result.append(c)
            j = prefix_matches[-1] if prefix_matches else 0

            while j > 0 and part[j] != c:
                j = lps[j - 1]
            
            if part[j] == c:
                j += 1
            
            prefix_matches.append(j)

            if j == len(part):  # If 'part' is found, remove it
                result = result[:-len(part)]
                prefix_matches = prefix_matches[:-len(part)]

        return "".join(result)


    def kmp(self,pattern):
        lps = [0] * len(pattern)
        
        for i in range(1, len(pattern)):
            prev_idx = lps[i - 1]
            
            while prev_idx > 0 and pattern[i] != pattern[prev_idx]:
                prev_idx = lps[prev_idx - 1]
            
            lps[i] = prev_idx + 1 if pattern[i] == pattern[prev_idx] else 0
        
        return lps


        