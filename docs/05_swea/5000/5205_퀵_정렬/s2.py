import sys
sys.stdin = open('input.txt', 'r')


for t in range(1,int(input())+1):
    N=int(input())
    n=list(map(int,input().split()))
    n.sort()
    print('#{} {}'.format(t,n[N//2]))