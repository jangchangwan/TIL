
H, M = map(int, input().split())
Mx = int(input())

H += Mx // 60
M += Mx % 60

if M >= 60:
    H += 1
    M -= 60

if H >= 24:
    H -= 24

print(H, M)