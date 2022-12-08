# 2935_소음

a = list(input() for _ in range(3))
if a[1] == "+":
    print(int(a[0])+int(a[2]))
else:
    print(int(a[0])*int(a[2]))