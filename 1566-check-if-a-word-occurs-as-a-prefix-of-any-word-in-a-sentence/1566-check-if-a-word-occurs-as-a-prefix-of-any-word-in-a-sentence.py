class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        a=sentence.split(" ")
        for i in range(len(a)):
            if a[i].startswith(searchWord):
                return i+1
        return -1
        