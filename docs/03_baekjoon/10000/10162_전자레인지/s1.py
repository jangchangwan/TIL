# 10162_전자레인지_문제풀이
# 2022-04-29

# 그리디알고리즘의 간단한 문제 유형

N = int(input())
ans = [0, 0, 0]
a = [300, 60, 10]
for i in range(3):
    ans[i] = N // a[i]
    N %= a[i]

if N:
    print(-1)
else:
    print(*ans)