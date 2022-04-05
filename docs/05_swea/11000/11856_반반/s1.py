import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1,T+1):
    ans = 'No'
    if len(set(input())) == 2:ans = 'Yes'
    print(f'#{t} {ans}')
