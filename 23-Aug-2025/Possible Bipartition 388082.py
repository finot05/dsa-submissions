# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d_map = defaultdict(list)
        for i, j in dislikes:
            d_map[i].append(j)
            d_map[j].append(i)

        colors = {}
        for p in range(1, n+1):
            if p not in colors:
                q = deque([(p, 'b')])
                while q:
                    m, c = q.popleft()
                    if m in colors:
                        if c != colors[m]:
                            return False
                        continue
                    colors[m] = c
                    new_c = 'r' if c == 'b' else 'b'
                    for negh in d_map[m]:
                        q.append((negh, new_c))
        return True