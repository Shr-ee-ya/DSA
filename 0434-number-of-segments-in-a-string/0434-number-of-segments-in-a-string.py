class Solution(object):
    def countSegments(self, s):
        if s.isspace() or len(s)==0:
            return 0
        else:
            a=s.split()
            return len(a)
        