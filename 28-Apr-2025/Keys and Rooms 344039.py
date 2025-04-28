# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        que = deque([0])
        visited = {0}
        while que:
            node = que.popleft()
            for nei in rooms[node]:
                if nei not in visited:
                    visited.add(nei)
                    que.append(nei)
        return len(visited) == n
