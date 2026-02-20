from typing import List, Optional

class Card:
    def __init__(self, value: int, prev: Optional['Card'] = None):
        self.value = value      # 현재 카드의 숫자
        self.prev = prev        # 왼쪽 pile의 top 카드 (즉, 이전 수열의 카드)

    def __repr__(self):
        return str(self.value)

class PatienceSortLIS:
    def binary_search_pile(self, piles: List[List[Card]], value: int) -> int:
        """
        현재 value를 어떤 pile에 올릴지 결정하는 이진 탐색.
        가장 왼쪽에서 가능한 pile을 찾는다.
        """
        left, right = 0, len(piles) - 1
        while left <= right:
            mid = (left + right) // 2
            top = piles[mid][-1]
            if top.value < value:
                left = mid + 1
            else:
                right = mid - 1

        # left가 가리키는 위치가 올릴 수 있는 위치
        return left

    def run(self, arr: List[int]) -> int:
        """
        전체 수열을 patience sorting 방식으로 처리
        각 수에 대해 적절한 pile을 찾아서 올리고, 연결 정보를 저장함
        최종적으로 pile의 개수가 LIS의 길이
        """
        piles: List[List[Card]] = []

        for num in arr:
            idx = self.binary_search_pile(piles, num)

            # 왼쪽 pile에서 가장 최근 카드 연결 (있다면)
            prev_card = piles[idx - 1][-1] if idx > 0 else None

            new_card = Card(num, prev_card)

            if idx == len(piles):
                # 새 pile 필요
                piles.append([new_card])
            else:
                # 기존 pile에 추가
                piles[idx].append(new_card)

        return len(piles)

# 입력 처리 및 실행 (BOJ 11053 맞춤)
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    solver = PatienceSortLIS()
    print(solver.run(arr))
