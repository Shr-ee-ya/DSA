class Solution(object):
    def numberOfSpecialChars(self, word):
        count=0
        word=set(word)
        print(word)
        for i in word:
            if i.islower()== True and i.upper() in word:
                count+=1
            elif i.isupper()==True and i.lower() in word:
                count+=1
        return count//2