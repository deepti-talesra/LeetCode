class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        curr_color = image[sr][sc]
        if curr_color == color:
            return image
        curr = [[sr, sc]]
        image[sr][sc] = color
        
        while curr:
            new_layer = []
            for r, c in curr:
                check = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for cr, cc in check:
                    if cr >= 0 and cc >= 0 and cr < m and cc < n and image[cr][cc] == curr_color:
                        image[cr][cc] = color
                        new_layer.append((cr, cc))
            curr = new_layer
        return image
