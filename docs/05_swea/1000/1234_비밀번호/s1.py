# 1234_비밀번호_문제풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')

T = 10

for t in range(1, T+1):
    N, nums = map(str, input().split())
    # 리스트로 분리
    num_lst = list(nums)
    password = list()
    # 다 빼올때까지 반복한다
    while len(num_lst) != 0:
        # 비어있을경우 무조건 넣어준다
        if len(password) == 0:
            password.append(num_lst.pop())
            continue
        # 같을경우 둘다 제외시켜준다
        elif num_lst[-1] == password[-1]:
            num_lst.pop()
            password.pop()
            continue
        # 위 조건 둘 다 아닐 경우 뺀값을 더해준다
        password.append(num_lst.pop())
    ans = password[::-1]
    print('#{}'.format(t), end=' ')
    print(*ans, sep='')
