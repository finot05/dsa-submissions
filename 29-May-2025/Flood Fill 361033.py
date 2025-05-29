# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        dir = [(-1, 0), (0 , -1) , (1, 0), (0, 1)]
        org = image[sr][sc]
        image[sr][sc] = color
        que = deque([(sr, sc)])
        while que:
            for _ in range(len(que)):
                sr , sc = que.popleft()
                for dr, dc in dir:
                    nr , nc = dr + sr , dc + sc
                    if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                        if image[nr][nc] != org:
                            continue
                        if image[nr][nc] != color:
                            image[nr][nc] = color
                            que.append((nr, nc))
        return image