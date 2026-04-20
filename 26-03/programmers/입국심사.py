def solution(n, times):
    times.sort()

    #최소 시간: 1초(혹은 0초)
    left = 0
    #최대 시간: 제일 느린 심사관이 n명을 혼자 처리하는 시간
    right = times[-1] * n

    answer = right

    while left <= right:
        #"이시간(mid)" 안에 n명 처리 가능?
        mid = (left + right) // 2

        processed = 0
        for t in times:
            processed += mid // t
            if processed >= n:
                break

        if processed >= n:
            answer = mid
            # 가능하면 시간을 줄여본다 (최소를 찾기 위해)
            right = mid - 1
        else:
            # 불가능하면 시간을 늘린다
            left = mid + 1

    return answer
