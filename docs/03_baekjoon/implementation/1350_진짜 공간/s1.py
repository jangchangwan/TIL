# 1350_진짜 공간
# 2022-09-02

N = int(input())

arr = list(map(int, input().split()))
number = int(input())

result = 0
for data in arr:
    a = data // number
    b = data % number
    if b:
        result += a * number + number
    else:
        result += a * number

print(result)