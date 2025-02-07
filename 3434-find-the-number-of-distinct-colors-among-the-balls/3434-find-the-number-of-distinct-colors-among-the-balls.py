class Solution(object):
    def queryResults(self, limit, queries):
        ball_colors = {}  # Stores the latest color of each ball
        color_count = {}  # Tracks the frequency of each color
        result = []

        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                if old_color in color_count:
                    color_count[old_color] -= 1  # Decrease old color count
                    if color_count[old_color] == 0:
                        del color_count[old_color]  # Remove color if no more balls use it

            ball_colors[x] = y  # Assign new color to ball x
            color_count[y] = color_count.get(y, 0) + 1  # Increase new color count

            result.append(len(color_count))  # Number of distinct colors

        return result

        '''
        balls= {} 
        unique= set()
        res= []

        for x, y in queries:
            if x in balls:
                old_color = balls[x]
                if old_color in unique:
                    unique.discard(old_color)  

            balls[x] = y  
            unique.add(y)  
            res.append(len(unique)) 
        return res
    '''
        