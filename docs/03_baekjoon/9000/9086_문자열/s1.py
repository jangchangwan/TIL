# 9086_문자열_문제풀이
# 2022-06-05

# 문자열의 첫번째는 인덱스가 0  마지막은 인덱스가 -1이다.

# 시행횟수
T = int(input())

# 시행횟수만큼 반복
for tc in range(T):
    # 문자열 입력받기
    word = input()
    # 첫글자와 끝글자 담기
    ans = word[0] + word[-1]
    print(ans)