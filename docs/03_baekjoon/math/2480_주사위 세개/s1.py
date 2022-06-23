# 2480_주사위 세개
# 2022-02-16

x1, x2, x3 = map(int,input().split())

if x1 == x2 == x3:
    print(10000+x1*1000)

elif x1 == x2:
    print(1000+x1*100)
elif x1 == x3:
    print(1000 + x1 * 100)
elif x2 == x3:
    print(1000 + x2 * 100)
else:
    print(max(x1, x2, x3)*100)