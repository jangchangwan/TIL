# 4873_반복문자_지우기_문제풀이
# 2022-02-22
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T+1):
    words = list(map(str, input()))
    result = list()
    # 문자열을 다 검열할때 까지 반복한다
    while len(words) != 0:
        # result 에 아무값도 없을경우 더해준다
        if len(result) == 0:
            result.append(words.pop())
            continue
        # words 의 끝값과 result 의 끝값이 같을경우
        elif words[-1] == result[-1]:
            # 둘다 버린다.
            words.pop()
            result.pop()
            continue
        # 위 조건이 모두 만족안할경우 그값을 더해준다.
        result += words.pop()
    ans = len(result)
    print('#{} {}'.format(t, ans))




