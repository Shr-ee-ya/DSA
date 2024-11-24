class Solution(object):
    def isValid(self, word):
        vowels = set("aeiouAEIOU")
        cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        
        if len(word) < 3:
            return False

        has_vowel = False
        has_cons = False
        for i in word:
            if i.isdigit():
                continue
            elif i in vowels:
                has_vowel=True
            elif i in cons:
                has_cons=True
            else:
                return False
        return has_vowel and has_cons
