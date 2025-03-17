class Solution(object):
    def divideArray(self, nums):
        hash_map={}
        for i in nums:
            if i in hash_map.keys():
                hash_map[i]+=1
            else:
                hash_map[i]=1

        for i in hash_map.values():
            if i%2!=0:
                return False
        return True        