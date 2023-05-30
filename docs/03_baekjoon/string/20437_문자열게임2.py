'''
문자열 W, 양의정수 K

어떤 문자가 K개 포함하는 가장 짧은 연속 문자열 길이 구하기
어떤 문자를 정확히 K를 포함하고 , 문자열 처음과 끝이 해당문자로 같은 가장 긴 연속 문자열의 길이 구한다

위 게임을 T 번 진행
'''
import sys
input = sys.stdin.readline

# 반복 횟수
T = int(input())

for tc in range(T):
    # 입력
    W = input().rstrip()
    K = int(input())
    
    # 변수
    count_dict = dict()
    check_dict = dict()
    flag = False
    min_value = len(W)
    max_value = -1
    
    for c in W:
        count_dict[c] = count_dict.get(c, 0) + 1
    
    # 실행
    for i in range(len(W)):
        if count_dict[W[i]] >= K:
            flag = True
            check_dict[W[i]] = check_dict.get(W[i], []) + [i]
    
    for key, value_list in check_dict.items():
        for i in range(len(value_list) - K + 1):
            min_value = min(min_value, value_list[i + K - 1] - value_list[i] + 1)
            max_value = max(max_value, value_list[i + K - 1] - value_list[i] +1)
    
    # 출력
    if flag:
        print(min_value, max_value)
    else:
        print(-1)    
    