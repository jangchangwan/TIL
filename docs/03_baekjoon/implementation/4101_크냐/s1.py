# 4101_크냐?_문제풀이
# 2022-06-05


while True:
    # 두 수 입력받기
    first, second = map(int, input().split())

    # 종료 조건
    if first == 0 and second == 0:
        break
    # 첫 번째 수가 클경우
    if first > second:
        print('Yes')
    # 아닐 경우
    else:
        print('No')