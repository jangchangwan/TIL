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
    # 양 쪽끝 2칸은 0이므로 2부터 시작해서 apt_cnt-2까지로 설정한다.
    for idx in range(2, apt_cnt-2):
        # 양쪽의 2칸의 값중 최대값을 구한다.
        max_apt = 0
        for i in range(idx-2, idx+3):
            if i != idx:
                if apt_list[i] > max_apt:
                    max_apt = apt_list[i]

        # 양쪽으로 2칸씩 자기보다 작을경우 조양권을 얻는다!
        if apt_list[idx] > apt_list[idx-2] and apt_list[idx] > apt_list[idx-1]:
            if apt_list[idx] > apt_list[idx+1] and apt_list[idx] > apt_list[idx+2]:
                result += apt_list[idx] - max_apt

    print('#{} {}'.format(t, result))
