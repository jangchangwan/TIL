# 19947_투자의 귀재 배주형
# 2022-06-20

money, year = map(int, input().split())

moneys = [0]*(year+1)
moneys[0] = money

for i in range(1, year+1):
    if i >= 5:
        moneys[i] = max(int(moneys[i-1] * 1.05), int(moneys[i-3] * 1.2), int(moneys[i-5] * 1.35))
    elif i >= 3:
        moneys[i] = max(int(moneys[i-1] * 1.05), int(moneys[i-3] * 1.2))
    else:
        moneys[i] = int(moneys[i-1] * 1.05)

print(moneys[year])