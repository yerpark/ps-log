from typing import List     # 타입 힌트 줄 수 있게 해주는 모듈 (like 정적 타입 언어처럼)

class Card:
    def __init__(self, value: int, prev: 'Card' = None):
        self.value = value
        self.prev = prev #이전의 카드를 가리킴 
    
    def __repr_(self):
        return str(self.value)
    
class LongestIncreasingSubsequence:
    def binary_search_host_pile_idx(self, piles: List[List[Card]], value: int) -> int:
