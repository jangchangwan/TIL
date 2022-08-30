# 4562_No Brainer
# 2022-07-26

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    if a < b:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")