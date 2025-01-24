class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        from collections import Counter

        max_freq = Counter()
        for word in words2:
            max_freq |= Counter(word)

        result = []
        for word in words1:
            freq = Counter(word)
            if all(freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)

        return result
