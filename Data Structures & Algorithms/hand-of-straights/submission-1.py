from heapq import heapify, heappush, heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sorted Set gives the start of hands
        # freq counter gives the available cards
 
        if len(hand) % groupSize != 0:
            return False

        card_count = {}
        for c in hand:
            card_count[c] = 1 + card_count.get(c, 0)
        
        starts = list(card_count.keys() )
        heapify(starts)
        
        while starts:
            cur = starts[0]
            for _ in range(groupSize):
                if cur not in card_count:
                    return False
                
                card_count[cur] -= 1
                if card_count[cur] == 0:
                    if cur != starts[0]:
                        return False
                    heappop(starts)
                cur += 1
        return True 