# 2005_파스칼의_삼각형_문제풀이
# 2022-02-21

import sys
sys.stdin = open('input.txt', 'r')


# 재귀로 풀어보기
def pascal_tri(num):
    # 1 일경우
    if num == 1:
        return [1]
    else:
        # 처음은 무조건 1로 시작하므로 [1] 리스트로 추가한다
        new_list = [1]
        # 재귀 호출
        last_list = pascal_tri(num - 1)
        # 중간값 인덱스 1의 값은  이전 리스트의 인덱스 0, 1의 합이다
        for i in range(len(last_list) - 1):
            new_list.append(last_list[i] + last_list[i + 1])
        # 마지막은 무조건 1로 끝나므로 1을 추가한다
        new_list += [1]
    return new_list


# 반복횟수
T = int(input())

for t in range(1, T + 1):
    # 입력값 받아오기
    num = int(input())
    print('#{}'.format(t))
    for i in range(1, num + 1):
        print(*pascal_tri(i))