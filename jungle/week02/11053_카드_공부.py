from typing import List

class Card:
    def __init__(self, value:int, prev: 'Card' = None):
        self.value = value
        self.prev = prev

class PatienceSortLIS:
    def binary_search_pile(self, piles: List[List[Card]], value: int) -> int:
        left = 0
        right = len(piles) - 1

        while left <= right:
            mid = (left + right) // 2
            if piles[mid][-1].value < value:
                left = mid + 1
            else:
                right = mid - 1
        
        return left if left < len(piles) else -1
    
    def run(self, arr: List[int]) -> int:
        piles = []

        for num in arr:
            idx = self.binary_search_pile(piles, num)
            prev_card = piles[idx - 1][-1] if idx > 0 else None
            new_card = Card(num, prev_card)

            if idx == -1:
                piles.append([new_card])
            else:
                piles[idx].append(new_card)
        
        return len(piles)
    

if __name__ == "__main__":
    n = int(input())

