T = int(input())

c1, c2 = 0, 0

for tc in range(T):
    if int(input()) == 1:
        c1 += 1
    else:
        c2 += 1

if c1 > c2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
