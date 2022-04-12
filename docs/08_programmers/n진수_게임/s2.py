# n진수_게임_문제풀이
# 2022-04-12


def convert(num, base):
    temp = "0123456789ABCDEF"
    #
    q, r = divmod(num, base)
    # 몫이 0 인경우 바로 반환
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]


def solution(n, t, m, p):
    answer = ''
    ans = ''
    # 마지막번호였을 경우 최대갯수
    for i in range(m * t):
        ans += str(convert(i, n))

    while len(answer) < t:
        answer += ans[p - 1]
        p += m

    return answer




print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))