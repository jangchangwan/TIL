import sys
sys.stdin = open('input_2.txt', 'r')


def x_y_sum(row, col):
    if row == 1 and col == 1:
        return 1
    else:
        i, j, cnt, res = 1, 1, 1, 1
        while i != row:
            i += 1
            res += cnt
            cnt += 1
        cnt += 1
        while j != col:
            j += 1
            res += cnt
            cnt += 1
        return res


def num_change(n):
    if n == 1:
        return 1, 1
    else:
        i, j, cnt, res = 1, 1, 1, 1
        while res < n:
            i += 1
            res += cnt
            cnt += 1
        i -= 1
        res -= (cnt - 1)
        while res != n:
            i -= 1
            j += 1
            res += 1
        return i, j


T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    x1, y1 = num_change(a)
    x2, y2 = num_change(b)
    xy = [x1+x2, y1+y2]
    ans = 1 + (xy[0] + xy[1] - 1)*(xy[0] + xy[1] - 2)//2 +xy[0] -1
    # ans = x_y_sum(x1+x2, y1+y2)
    print('#{} {}'.format(tc, ans))