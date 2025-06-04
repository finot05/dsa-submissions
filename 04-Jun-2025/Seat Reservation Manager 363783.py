# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.avail = [] 
        self.next = 1
        self.n = n

    def reserve(self) -> int:
        if self.avail:
            return heapq.heappop(self.avail)
        else:
            seat = self.next
            self.next += 1
            return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.avail, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)