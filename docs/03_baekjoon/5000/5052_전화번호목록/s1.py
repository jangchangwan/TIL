# 5052_전화번호_목록_문제풀이
# 2022-04-26

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    phone_lst = list(input() for _ in range(N))
    ans = 'YES'
    phone_lst.sort()
    for i in range(N - 1):
        # 같을경우 뒤에번호를 전화를 걸 방법이없으므로 No출력
        if phone_lst[i + 1][:len(phone_lst[i])] == phone_lst[i]:
            ans = 'NO'
            break
    print(ans)