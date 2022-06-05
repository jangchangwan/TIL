# 2744_대소문자 바꾸기_문제풀이
# 2022-06-05

word = input()

# isupper() : 대문자일시 True 반환 아닐경우 False
# lower() : 소문자로 변환
# upper() : 대문자로 변환

# 결과를 담을 문자열
ans = ''
for w in word:
    # 대문자 인 경우
    if w.isupper():
        ans += w.lower()
    # 소문자 인 경우
    else:
        ans += w.upper()

# 결과 출력
print(ans)