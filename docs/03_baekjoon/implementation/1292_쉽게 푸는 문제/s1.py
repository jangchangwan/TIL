# 1292_쉽게 푸는 문제
# 2022-08-27

start, end = map(int, input().split())

arr = []
count = 0
while len(arr) <= 1000:
    count += 1
    cnt = 0
    while True:
        if count == cnt:
            break
        cnt += 1
        arr.append(count)

print(sum(arr[start-1:end]))