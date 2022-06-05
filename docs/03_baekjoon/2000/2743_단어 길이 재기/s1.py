# 2743_단어 길이 재기_문제풀이
# 2022-06-05

# 단어 입력받기
word = input()

# 1. for문으로 문자 카운팅
cnt = 0
for w in word:
    cnt += 1

# 2. 내장함수 사용
cnt = len(word)

# 출력
print(cnt)