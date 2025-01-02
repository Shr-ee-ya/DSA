class Solution(object):
    def vowelStrings(self, words, queries):
        def is_vowel(c):
            return c in {'a','e','i','o','u'}

        vowel=[]
        for i in words:
            if is_vowel(i[0]) and is_vowel(i[-1]):
                vowel.append(1)
            else:
                vowel.append(0)

        summ=[0]
        for count in vowel:
            summ.append(summ[-1]+count)

        results=[]
        for l,r in queries:
            results.append(summ[r+1]-summ[l])

        return results

        