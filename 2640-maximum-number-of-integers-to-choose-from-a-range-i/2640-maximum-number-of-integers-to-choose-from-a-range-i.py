class Solution(object):
    def maxCount(self, banned, n, maxSum):
        banned_set=set(banned) 
        curr_sum=0
        count=0

        for i in range(1, n+1):
            if i not in banned_set and curr_sum+i<=maxSum:
                curr_sum+=i
                count+=1
            elif curr_sum+i>maxSum:
                break
        return count


        '''
        not_banned=[]
        if max(banned)>n:
            for i in range(1,n+1):
                if i not in banned:
                    not_banned.append(i)
        else:
            for i in range(1,n):
                if i not in banned:
                    not_banned.append(i)

        
        if len(not_banned)==0:
            return 0
        else:
            curr_sum=0
            count=0
            for i in not_banned:
                if curr_sum +i <=maxSum:
                    curr_sum +=i
                    count+=1
                else:
                    break
            return count  '''



        