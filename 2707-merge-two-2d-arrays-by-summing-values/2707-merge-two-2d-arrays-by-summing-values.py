class Solution(object):
    def mergeArrays(self, nums1, nums2):
        merged = []
        added = set()

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i][0] == nums2[j][0]:
                    nums1[i][1] += nums2[j][1]
                    added.add(nums2[j][0]) 

        for pair in nums2:
            if pair[0] not in added:  
                nums1.append(pair)

        return sorted(nums1)
