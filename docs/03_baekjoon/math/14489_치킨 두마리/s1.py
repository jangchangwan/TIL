# 14489_치킨 두마리
# 2022-06-18


a, b = map(int, input().split())
price = int(input())

estimated_price = (a + b)

if price*2 <= estimated_price:
    print(a+b - price*2)
else:
    print(a+b)