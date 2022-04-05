import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    P,Q,R,S,W=map(int,input().split())
    total_A,total_B= P * W,Q
    if W > R:total_B = Q + (W-R) * S
    print(f'#{t} {min(total_A, total_B)}')