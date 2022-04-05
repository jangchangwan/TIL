# 2005_파스칼의_삼각형_문제풀이
# 2022-02-21

import sys
sys.stdin = open('input.txt', 'r')


# Memoization 으로 풀어보기
def pascal_tri(Num):
    # 외부 pascal_data 불러오기
    global pascal_data
    # 인덱스 0,1 은 만들어 놨으므로  그 이상의 경우만 동작하게만듬
    # 추가로 또 동작했을 경우 이전 데이터를 재활용 하기위해 만듬
    if Num >= 2 and len(pascal_data) <= Num:
        new_list = [1]
        old_list = pascal_data[Num-1]
        # 중간값
        for i in range(len(old_list) - 1):
            new_list.append(old_list[i] + old_list[i + 1])
        new_list += [1]
        pascal_data.append(new_list)
    return pascal_data


T = int(input())
pascal_data = [[], [1]]
for t in range(1, T+1):

    N = int(input())
    ans = pascal_tri(N)
    print('#{}'.format(t))
    for i in range(1,N+1):
        print(*pascal_data[i])