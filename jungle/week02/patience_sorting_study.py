from typing import List

class Card:
    # 뭔가 생성자리스트 느낌인데 None이 Null인가? 
        # ✅ prev를 forward reference해준 것. 여기에 card 포인터가 들어갈건데 아직은 none
    def __init__(self, value:int, prev: 'Card' = None): 
        self.value = value
        self.prev = prev
    
    # repr 이거 뭐였더라.. representation? 자기 자신 설명..?
        # ✅ print하거나 디버깅할 때 객체가 어떻게 보일지 정의하는 함수 
    def __repr__(self):
        return str(self.value)
    
class LongestIncreasingSubsequence:
    # 이것또한 파라미터 자료형 구체적으로 담은건가? 원래 파이썬에선 필요없지만
    # 가독성을 위해서?

    # -> 이건 Return value type 명시?
    def binary_search_host_pile_idx(self, piles: List[List[Card]], value:int) -> int: 
        left = 0
        right = len(piles) - 1

        #현재 파일 더미에 아무것도 없음. 최초의 파일 더미를 만들어야 함
        if not piles:
            return -1
        
        while left <= right :
            mid = left + (right - left) // 2 # int 오버플로우 방지 -> 파이썬에서 필요한가?
            top_card = piles[mid][-1]
            #파일 더미에서 가장 작은 값이 맨 뒤에 저장되어 있는 구존가?
                # ✅ NO!!! 파일더미는 작은 값들이 처음부터 차곡차곡 쌓임
                    # 가장 최근에 쌓인 카드, 즉 맨 뒤에 있는 카드가 -1 

            # 이분탐색의 작동 방식? 모습을 모르겠네.. 
            if top_card.value < value:
                left = mid + 1
                # 응? 그냥 이 때 이 파일더미 리턴하는게 맞지 않나..? 왜지 ?
            else:
                right = mid - 1
            
        # 아래 조건문과 리턴의 의미를 전혀 모르겠음. .
        if left >= len(piles):
            return -1
        
        # 이것도 지금 전혀 모르겠는 상태 .. 
        return left if piles[left][-1].value > value else - 1

    def retrieve_seq(self, piles: List[List[Card]]) -> List[int]:
        seq = []
        card = piles[-1][0] # 마지막 더미의 첫번째 카드만 봄 (왜지? 댜른 카드들은 안봐도 되나?)

        while card :
            seq.append(card.value)
            card = card.prev
        
        return seq[::-1] #카드 뒤집기 
    
    def run(self, arr:List[int]) -> List[int]:
        piles: List[List[Card]] = [] # 이런 형태 처음봄 이거 멤버변순가 뭔가

        for value in arr:
            host_idx = self.binary_search_host_pile_idx(piles, value)
        
            if host_idx == -1 :
                host_pile = []
                piles.append(host_pile)
                host_idx = len(piles) - 1
            else :
                host_pile = piles[host_idx]
            
            #근데 잠깐 의문 : host_pile의 역할은 ? 새로운 카드를 추가할 해당 더미인가?
            
            prev_card = None
            if (host_idx > 0):
                prev_card = piles[host_idx - 1][-1]
                #왜 맨 마지막 애만 보는거지?
                #왼쪽 애의 왜 맨 마지막 원소만..?
                #그래서 마지막 원소가 제일 큰건지 작은건지도 헷갈림
            
            host_pile.append(Card(value, prev_card))
        
        return self.retrieve_seq(piles)
