T=int(input())
for t in range(1,T+1):
    A,B=map(int,input().split())
    if A>B:ans='>'
    elif A<B:ans='<'
    else:ans='='
    print('#{} {}'.format(t,ans))
