class Solution(object):
    def maxChunksToSorted(self, arr):
        sarr = sorted(arr)
        count = 0  # To count the number of chunks
        current_sum_arr = 0  # Running sum of elements in arr
        current_sum_sarr = 0  # Running sum of elements in sarr

        for i in range(len(arr)):
            current_sum_arr += arr[i]
            current_sum_sarr += sarr[i]
            
            # Compare running sums to determine if a chunk can be formed
            if current_sum_arr == current_sum_sarr:
                count += 1

        return count


        """
        if arr==sorted(arr):
            return len(arr)
        if arr==sorted(arr, reverse=True):
            return 1
        else:
            count=0
            sarr=sorted(arr)
            for i in range(len(arr)):
                if arr[i]!=sarr[i]:
                    count+=1
            return len(arr)-count +1
            """
        