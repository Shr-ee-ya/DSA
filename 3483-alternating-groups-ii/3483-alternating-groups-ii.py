class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        count = 0
        invalid_count = 0

        for i in range(k - 1):
            if colors[i] == colors[i + 1]:
                invalid_count += 1

        if invalid_count == 0:
            count += 1

        for i in range(1, n):
            if colors[(i - 1) % n] == colors[i % n]:
                invalid_count -= 1

            if colors[(i + k - 2) % n] == colors[(i + k - 1) % n]:
                invalid_count += 1

            if invalid_count == 0:
                count += 1

        return count
