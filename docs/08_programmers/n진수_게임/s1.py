# n진수_게임_문제풀이
# 2022-04-12
from collections import deque


def solution(n, t, m, p):
    answer = ''
    queue = deque([])
    num = 0
    order = 0
    while t > 0:
        if not queue:
            queue = deque(list(base_n(num, n)))
            num += 1
        char = queue.popleft()
        if order % m == (p - 1):
            answer += char
            t -= 1
        order += 1
    return answer


def base_n(num, n):
    result = ""
    alpha = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    if num == 0:
        return "0"
    while num > 0:
        char = num % n
        if char >= 10:
            char = alpha[char]
        else:
            char = str(char)
        result = char + result
        num //= n
    return result


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))