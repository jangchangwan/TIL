# 1427_소트인사이드
# 2022-06-20

data = list(map(int, input()))

data.sort(reverse=True)
for i in data:
    print(i, end='')
print()