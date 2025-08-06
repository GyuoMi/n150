# slower iterative solution ?? NO, leetcode is weird
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: 
        m, n = len(image), len(image[0])
        init_color = image[sr][sc]

        if init_color == color:
            return image

        queue = collections.deque([(sr, sc)])
        image[sr][sc] = color
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and image[new_r][new_c] == init_color:
                    image[new_r][new_c] = color
                    queue.append((new_r, new_c))
        return image


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ret = self.search(image, sr, sc, color, image[sr][sc])
        return ret

    def search(self, image: List[List[int]], sr: int, sc: int, color: int, target: int) -> List[List[int]]:
        # within m x n 
        while 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] != color and image[sr][sc] == target:
            image[sr][sc] = color
            # go to neighbors
            image = self.search(image, sr - 1, sc, color, target)
            image = self.search(image, sr + 1, sc, color, target)
            image = self.search(image, sr, sc - 1, color, target)
            image = self.search(image, sr, sc + 1, color, target) 

            return image
        return image
      

