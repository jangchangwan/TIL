# 괄호 변환
# 2022-04-24

'''

'()', ')(' 로만 이루어진 문자열이 있고 ), ( 의 개수가 같다면 균형잡힌 괄호문자열
그리고 그 괄호의 짝도 모두 맞을 경우에는 올바른 괄호 문자열 이라고 한다

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.

'''

# 올바른 문자열인지 체크
def balance_string(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i



# 올바른 문자열인지 체크
def check_proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0: # 쌍이 맞지 않을 경우 False
                return False
            cnt -= 1
    return True # 쌍이 맞을 경우 True


def solution(p):
    answer = ''
    # 공백일 경우 공백 출력
    if p == '':
        return answer
    index = balance_string(p) # 괄호가 전체적으로 맞는 부분의 인덱스 확인
    # 그 인덱스를 기준으로 나눔
    u = p[:index+1]
    v = p[index+1:]

    # 올바른문자열일경우
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫번째 문자와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)
    return answer




print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))