class Solution(object):
    def isArraySpecial(self, nums, queries):

        n = len(nums)
    # Step 1: Precompute adjacent parity differences
        is_special = [0] * (n - 1)
        for i in range(n - 1):
            is_special[i] = 1 if nums[i] % 2 != nums[i + 1] % 2 else 0

        # Step 2: Build a prefix sum over the `is_special` array
        special_prefix = [0] * n
        for i in range(1, n):
            special_prefix[i] = special_prefix[i - 1] + is_special[i - 1]

        # Step 3: Answer each query
        res = []
        for fromi, toi in queries:
            # Check if the range is special
            if toi == fromi:
                # Single-element subarrays are always special
                res.append(True)
            else:
                # Count the number of special pairs in the range
                special_pairs = special_prefix[toi] - special_prefix[fromi]
                # If all pairs are special, the subarray is special
                res.append(special_pairs == toi - fromi)
        return res




        '''
        subnums = []
        for i in range(len(queries)):
            sublist = []
            for j in range(queries[i][0], queries[i][1] + 1):
                sublist.append(nums[j])
            subnums.append(sublist)

        #print(subnums) 

        res = []
        for sublist in subnums:
            if len(sublist) == 1:  # Single-element subarrays are always special
                res.append(True)
            else:
                is_special = True  # Assume the subarray is special
                for k in range(len(sublist) - 1):
                    # Check if adjacent elements have the same parity
                    if (sublist[k] % 2 == 0 and sublist[k + 1] % 2 == 0) or (sublist[k] % 2 != 0 and sublist[k + 1] % 2 != 0):
                        is_special = False
                        break
                res.append(is_special)
        
        return res
'''