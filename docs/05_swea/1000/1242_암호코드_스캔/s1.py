# 1242_암호코드_스캔_문제풀이
# 2022-03-24

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# 뒤에서부터 봐야하므로 패턴번호도 뒤에서부터 적어준다
# 맨앞에 0의 갯수는 보지 않는다.
my_patten = {
    '112': 0, '122': 1, '221': 2,
    '114': 3, '231': 4, '132': 5,
    '411': 6, '213': 7, '312': 8,
    '211': 9,
}

# 16진수 딕셔너리
my_hex = {
    '0': '0000',    '1': '0001',    '2': '0010',    '3': '0011',
    '4': '0100',    '5': '0101',    '6': '0110',    '7': '0111',
    '8': '1000',    '9': '1001',    'A': '1010',    'B': '1011',
    'C': '1100',    'D': '1101',    'E': '1110',    'F': '1111',
}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # arr = [list(map(str, input())) for _ input.txt range(N)]
    # set 을 통해 중복되는 경우 다 없애기
    arr = list(set([input()[:M] for _ in range(N)]))
    # print(arr)
    # set 으로 배열을 줄였으므로 배열의 길이을 다시 받아오기
    N = len(arr)
    # 16진수 -> 2진수 변환
    binary_lst = [''] * N
    for i in range(N):
        for j in range(M):
            binary_lst[i] += my_hex[arr[i][j]]
    # 암호코드 저장할 공간
    temp = []
    visited = []
    ans = 0
    # 암호코드 찾기
    for n in range(N):
        pattern_1, pattern_2, pattern_3 = 0, 0, 0
        # 뒤에서 부터 시작
        for m in range(M*4-1, -1, -1):
            # 1번째 패턴
            if pattern_2 == 0 and pattern_3 == 0 and binary_lst[n][m]=='1':
                pattern_1 += 1
            # 2번째 패턴
            elif pattern_1 > 0 and pattern_3 == 0 and binary_lst[n][m] =='0':
                pattern_2 += 1
            # 3번째 패턴
            elif pattern_1 > 0 and pattern_2 > 0 and binary_lst[n][m] =='1':
                pattern_3 += 1
            # 1,2,3 패턴 다찾고 0을 만나는 경우 암호코드 출력
            if pattern_1 > 0 and pattern_2 > 0 and pattern_3 > 0 and binary_lst[n][m] == '0':
                # 길이가 배수로 늘어날 경우 키값 에러 발생
                # 각 패턴값을 최소값만큼 나눠줘야한다
                min_pattern = min(pattern_1, pattern_2, pattern_3)
                pattern_1 //= min_pattern
                pattern_2 //= min_pattern
                pattern_3 //= min_pattern
                pattern = my_patten[str(pattern_1)+str(pattern_2)+str(pattern_3)]
                temp.append(pattern)
                # 초기화 : 같은줄에 여려 암호코드가 있을수 있기 때문에
                pattern_1, pattern_2, pattern_3 = 0, 0, 0
            # 코드 검증
            if len(temp) == 8:
                # 패턴은 반대로 넣었기 때문에 되돌려야한다.
                temp = temp[::-1]
                # 암호코드 합
                temp_sum = 0
                for i in range(8):
                    if i % 2:
                        temp_sum += temp[i]
                    else:
                        temp_sum += (temp[i] * 3)
                # 10의 배수이고 방문한 값이 아닐경우
                if temp_sum % 10 == 0 and temp not in visited:
                    ans += sum(temp)
                # 방문
                visited.append(temp)
                # 초기화 : 같은줄에 여려 암호코드가 있을수 있기 때문에
                temp = []

    print('#{} {}'.format(tc, ans))