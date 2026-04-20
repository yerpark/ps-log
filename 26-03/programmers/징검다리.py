def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    lo, hi = 1, distance
    answer = 0 

    while lo <= hi:
        mid = (lo + hi) // 2
        removed = 0
        prev = 0
        
        for r in rocks:
            if r - prev < mid:
                removed += 1
            else:
                prev = r
        
        if removed <= n:
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    return answer