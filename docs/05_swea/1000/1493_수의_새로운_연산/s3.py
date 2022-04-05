import sys
sys.stdin = open('input_2.txt', 'r')


def find(n):
    global d
    if n <= d[-1]:
        k = len(d)
        for i in range(len(d)-1, -1, -1):
            if d[i-1] < n <= d[i]:
                k = i
                break
        return [1+n-(1 + (k-1)*k//2), k-(n-(1 + (k-1)*k//2))]
    else:
        k = len(d)
        while True:
            if (1 + (k-1)*k//2) <= n <= k*(k+1)//2:
                break
            d.append(k*(k+1)//2)
            k += 1
        return [1+n-(1 + (k-1)*k//2), k-(n-(1 + (k-1)*k//2))]


d = [0]
res = []

for tc in range(int(input())):
    a, b = map(int, input().split())
    a_xy = find(a)
    b_xy = find(b)
    xy = [a_xy[0]+b_xy[0], a_xy[1]+b_xy[1]]
    ans = 1 + (xy[0]+xy[1]-1) * (xy[0]+xy[1]-2) // 2 +xy[0] - 1
    res.append("#{} {}".format(tc+1, ans))

print('\n'.join(res))