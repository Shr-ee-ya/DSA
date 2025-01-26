class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph=paragraph.lower()
        new_para=""
        for i in paragraph:
            if i.isalnum():
                new_para+=i
            else:
                new_para+=" "
        words=new_para.split()
        banned_set=set(banned)
        count= Counter(word for word in words if word not in banned_set)
        most_common_word, _ = count.most_common(1)[0]
        return most_common_word

        