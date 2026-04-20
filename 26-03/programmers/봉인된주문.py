from bisect import bisect_right

def solution(n, bans):
    alphabet = "abcdefghijklmnopqrstuvwxyxz"
    idx = {c:i + 1 for i, c in enumerate(alphabet)}

    def s2n(s):
        v = 0
        for ch in s:
            v = v * 26 + idx[ch]
        return v
    
    def n2s(x):
        res = []
        while x > 0:
            x -= 1
            res.append(alphabet[x % 26])
            x //= 26
        return "".join(reversed(res))
    
    ban_nums = sorted(s2n(s) for s in bans)

    target = n
    while True:
        deleted_cnt = bisect_right(ban_nums, target)
        new_target = n + deleted_cnt
        if new_target == target:
            break
        target = new_target
    
    return n2s(target)
