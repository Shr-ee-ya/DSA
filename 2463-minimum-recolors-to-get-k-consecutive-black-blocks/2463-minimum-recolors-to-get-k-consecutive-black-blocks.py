class Solution(object):
    def minimumRecolors(self, blocks, k):
        
        min_ops = blocks[:k].count('W')
        current_ops = min_ops

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_ops -= 1
            if blocks[i] == 'W':
                current_ops += 1
            min_ops = min(min_ops, current_ops)

        return min_ops

        