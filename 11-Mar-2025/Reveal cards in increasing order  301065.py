# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        dq = deque()
        for card in deck:
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(card)
        return list(dq)