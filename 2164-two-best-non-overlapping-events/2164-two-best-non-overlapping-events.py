class Solution(object):
    def maxTwoEvents(self, events):
        from bisect import bisect_left

        # Sort events by their end times
        events.sort(key=lambda x: x[1])

        # Prepare an array to store maximum values up to each event
        max_values = []
        max_so_far = 0

        # Iterate through events to build the max_values array
        for start, end, value in events:
            max_so_far = max(max_so_far, value)
            max_values.append((end, max_so_far))

        max_sum = 0

        # Iterate through events to calculate the maximum sum
        for start, end, value in events:
            # Binary search for the latest event that ends before the current event's start
            index = bisect_left(max_values, (start,)) - 1
            # If such an event exists, combine its maximum value with the current event's value
            if index >= 0:
                max_sum = max(max_sum, value + max_values[index][1])
            else:
                # Consider only the current event's value
                max_sum = max(max_sum, value)

        return max_sum
