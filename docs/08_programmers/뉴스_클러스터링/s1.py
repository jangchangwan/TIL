# 뉴스-클러스터링_문제풀이
# 2022-04-4

# 두글자씩 끊어서 원소를 만든다.


def solution(str1, str2):
    # 대소문자 차이는 무시하므로
    str1 = str1.lower()
    str2 = str2.lower()
    # print(str1, str2)

    # 문자열을 두글자씩 끊어서 비교
    # 문자가 아닌 숫자, 특수문자, 공백이 들어 올경우 제외시켜야 하므로
    # isalpha 함수를 사용한다.
    str1_lst = []
    str2_lst = []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            str1_lst.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            str2_lst.append(str2[i:i + 2])
    # print(str1_lst)
    # print(str2_lst)

    # 교집합 구하기
    inter_lst = []
    for i in range(len(str1_lst)):
        for j in range(len(str2_lst)):
            if str1_lst[i] == str2_lst[j] and str1_lst[i] != False and str2_lst[j] != False:
                inter_lst.append(str1_lst[i])
                str1_lst[i] = False
                str2_lst[j] = False
    # print(inter_lst)
    # 합집합은 두 집합의 갯수합 - 교집합이므로 따로 구현 X
    union_cnt = len(str1_lst) + len(str2_lst) - len(inter_lst)
    inter_cnt = len(inter_lst)
    # 출력
    if union_cnt == 0 and inter_cnt == 0:
        answer = 65536
    else:
        answer = int(inter_cnt / union_cnt * 65536)
    return answer








# 입력 예제
print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

# 출력 예제
#   16384
#	65536
#   43690
#   65536