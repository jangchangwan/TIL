# 11945_뜨거운 붕어빵
# 2022-06-18


N, M = map(int, input().split())

arr = [input() for _ in range(N)]

answer = []

for word in arr:
    answer.append(word[::-1])

for ans in answer:
    print(ans)