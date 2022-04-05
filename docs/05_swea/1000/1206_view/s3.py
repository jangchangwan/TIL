import sys

sys.stdin = open('input.txt', 'r')
# 시행횟수
T = 10
# 시행횟수 만큼 반복
for t in range(1, T+1):

    # 빌딩 데이터 받아오기
    apt_cnt = int(input())
    apt_list = list(map(int, input().split()))

    result = 0
    # 초기 인덱스 설정
    idx = 2

    while idx < apt_cnt-2:
        # 한칸 이동하는 경우
        if apt_list[idx] <= apt_list[idx-2] or apt_list[idx] <= apt_list[idx-1] or apt_list[idx] <= apt_list[idx+1]:
            idx += 1
        # 2칸씩 이동하는 경우 쓰자
        elif apt_list[idx] <= apt_list[idx+2]:
            idx += 2
        # 나머지의 경우 조망권을 획득하므로 result 에 더해준다
        else:
            # 양쪽 끝 최대값 구하기
            max_apt = 0
            for i in range(idx - 2, idx + 3):
                # idx 는 제외하고 양쪽의 max 값을 구하기 위해서
                if i != idx:
                    if apt_list[i] > max_apt:
                        max_apt = apt_list[i]
            result += apt_list[idx] - max_apt
            idx += 3
        
    print('#{} {}'.format(t, result))