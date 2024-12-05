class Solution(object):
    def canChange(self, start, target):
        n=len(start)
        s_idx=0
        t_idx=0

        if start.count("L")!=target.count("L"):
            return False
        if start.count("R")!=target.count("R"):
            return False
        while s_idx<n and t_idx<n:
            while s_idx<n and start[s_idx]=="_":
                s_idx+=1
            while t_idx<n and target[t_idx]=="_":
                t_idx+=1
            
            if s_idx==n and t_idx==n:
                return True
            if s_idx==n or t_idx==n:
                return False

            if (start[s_idx] !=target[t_idx]) or (start[s_idx]=="L" and s_idx<t_idx) or (start[s_idx]=="R" and s_idx> t_idx):
                return False
            s_idx+=1
            t_idx+=1
        return True
            

