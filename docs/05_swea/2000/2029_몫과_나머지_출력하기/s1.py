T=int(input())
for t in range(1,T+1):
    A,B=map(int,input().split())
    print('#{} {} {}'.format(t,A//B,A%B))