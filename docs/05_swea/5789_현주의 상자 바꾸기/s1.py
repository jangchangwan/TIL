import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())
    # 초기 박스 만들기
    box_list = [0] * N
    # 반복횟수
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        # L~R 사이의 값 변경
        for i in range(L-1, R):
            box_list[i] = q
    # 한줄로 표기하기위해서 end= 사용
    print('#{}'.format(t), end=' ')
    for box in box_list:
        print(box, end=' ')
    print()