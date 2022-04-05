# 1242_암호코드-스캔 풀이
# 2022-03-24

import sys
sys.stdin = open('input.txt', 'r')


def find_code(arr,N,M):
    code_list = []
    for i in range(N):
        if arr[i] in code_list:
            continue
        for j in range(M):
            if arr[i][j] != '0':
                code = arr[i]
                code_list.append(code)
                break
    return code_list


def hex_bin(code_list):
    bin_dict = {
        '0' : '0000', '1' : '0001', '2' : '0010',
        '3' : '0011', '4' : '0100', '5' : '0101',
        '6' : '0110', '7' : '0111', '8' : '1000',
        '9' : '1001', 'A' : '1010', 'B' : '1011',
        'C' : '1100', 'D' : '1101', 'E' : '1110',
        'F' : '1111',
    }
    bin_code_list = []
    for code in code_list:
        bin_code = ''
        for hex_num in code:
            bin_code += bin_dict[hex_num]
        bin_code_list.append(bin_code)
    return bin_code_list


def decode(bin_code_list):
    decode_dict = {
        '0001101' : 0, '0011001' : 1, '0010011' : 2,
        '0111101' : 3, '0100011' : 4, '0110001' : 5,
        '0101111' : 6, '0111011' : 7, '0110111' : 8,
        '0001011' : 9,
    }
    decode_list = []
    for bin_code in bin_code_list:
        i = len(bin_code)-1
        ############### while 문 시작 ####################
        while i > 0:
            if bin_code[i] == '1':
                j = i
                nums = []
                m = 1
                ######### while문 시작 ##############
                while True:
                    bin_num = bin_code[j-(7*m-1):j+1:m]

                    if decode_dict.get(bin_num) == None:
                        m += 1
                        j = i
                        continue
                    else:
                        nums = [decode_dict[bin_num]] + nums
                        j -= 7*m
                    if len(nums) == 8:
                        break
                ############  while 문 끝 ############
                if [nums, m, j] not in decode_list:
                    decode_list.append([nums, m, j])
                    i -= 56*m
                    continue
                else:
                    i -= 56*m
                    continue
            i -= 1
            ############### while 문 끝 ####################
    return decode_list


def check_and_sum(decode_list):
    ans_sum = 0
    for decode in decode_list:
        odd = 0
        even = 0
        for k in range(7):
            if k%2 == 0:
                odd += decode[0][k]
            else:
                even += decode[0][k]
        if (odd*3+even+decode[0][7]) % 10 == 0:
            ans_sum += sum(decode[0])
    return ans_sum


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    code_list = find_code(arr,N,M)
    bin_code_list = hex_bin(code_list)
    decode_list = decode(bin_code_list)
    ans = check_and_sum(decode_list)
    print('#{} {}'.format(t, ans))