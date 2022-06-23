# 가희와 방어율 무시_문제풀이
# 2022-06-08

a, b = map(int, input().split())

res = a * (100 - b) / 100

if res >= 100:
    print(0)
else:
    print(1)