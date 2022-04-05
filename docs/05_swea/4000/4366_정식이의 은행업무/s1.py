# 4366_정식이의_은행업무_문제풀이
# 2022-03-24
import sys
sys.stdin = open('input.txt', 'r')


def babo():
    for i in range(BIN):
        temp = bin_lst[i]
        # 2진수 한자리 변환
        bin_lst[i] = (temp + 1) % 2

        for j in range(TRI):
            temp3 = tri_lst[j]
            # 3진수 한자리 변환
            for k in range(1, 3):
                tri_lst[j] = (temp3 + k) % 3
                # 값 초기화
                bin_num = 0
                tri_num = 0
                # 2진수 값 계산
                for b in range(BIN):
                    if bin_lst[b] == 1:
                        bin_num += 2 ** (BIN-1 - b)
                # 3진수 값 계산
                for t in range(TRI):
                    if tri_lst[t] > 0:
                        tri_num += tri_lst[t] * (3 ** (TRI-1 - t))
                # 값이 같을 경우 출력
                if bin_num == tri_num:
                    return bin_num
            # 3진수 복구
            tri_lst[j] = temp3
        # 2진수 복구
        bin_lst[i] = temp
    return '못찾음'


T = int(input())
for tc in range(1, T+1):
    bin_lst = list(map(int, input()))
    tri_lst = list(map(int, input()))
    BIN = len(bin_lst)
    TRI = len(tri_lst)
    ans = babo()
    print('#{} {}'.format(tc, ans))