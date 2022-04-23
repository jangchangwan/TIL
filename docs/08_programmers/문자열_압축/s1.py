# 문자열_압축
# 2022-04-23

'''
s 의 길이 1 ~ 1000
소문자로만 구성

1000까지이므로 완전탐색으로 가능하다고 생각
압축할수있는 범위는 문자열길의 절반까지만 압축가능
1개 단위부터 len(s)//2 까지 압축해보고 최소값 출력

'''


def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2+1):
        result = ""
        prev = s[0:step]
        count = 1 # 압축 횟수
        for j in range(step, len(s), step):
            # 동일 패턴일시
            if prev == s[j:j+step]:
                count += 1
            # 패턴 X
            else:

                if count >= 2:
                    result += str(count) + prev
                else:
                    result += prev
                # 상태 초기화
                prev = s[j: j+step]
                count = 1
        # 남아 있는 문자열 처리
        if count >= 2:
            result += str(count) + prev
        else:
            result += prev
        answer = min(answer, len(result))
    return answer



print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

'''
출력예시
#1 7
#2 9
#3 8
#4 14
#5 17 
'''


'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.34ms, 10.3MB)
테스트 3 〉	통과 (0.17ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.36ms, 10.2MB)
테스트 8 〉	통과 (0.36ms, 10.2MB)
테스트 9 〉	통과 (0.59ms, 10.4MB)
테스트 10 〉	통과 (3.77ms, 10.3MB)
테스트 11 〉	통과 (0.08ms, 10.4MB)
테스트 12 〉	통과 (0.10ms, 10.2MB)
테스트 13 〉	통과 (0.09ms, 10.2MB)
테스트 14 〉	통과 (0.52ms, 10.2MB)
테스트 15 〉	통과 (0.10ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (1.08ms, 10.2MB)
테스트 18 〉	통과 (1.04ms, 10.2MB)
테스트 19 〉	통과 (1.02ms, 10.2MB)
테스트 20 〉	통과 (2.31ms, 10.2MB)
테스트 21 〉	통과 (2.38ms, 10MB)
테스트 22 〉	통과 (2.24ms, 10.3MB)
테스트 23 〉	통과 (2.18ms, 10.1MB)
테스트 24 〉	통과 (2.20ms, 10.4MB)
테스트 25 〉	통과 (2.40ms, 10.1MB)
테스트 26 〉	통과 (2.23ms, 10.2MB)
테스트 27 〉	통과 (2.38ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.2MB)

'''