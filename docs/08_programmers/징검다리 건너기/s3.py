def solution(stones, k):
    left, right = 1, 200000000

    while left < right:
        mid, cnt = (left + right) // 2, 0
        for t in stones:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid
        else:
            left = mid + 1

    return left