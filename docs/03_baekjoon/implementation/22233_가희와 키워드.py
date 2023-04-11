import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = dict()
for _ in range(n) :
    board[input().rstrip()] = 1
    
res = n
for _ in range(m) :
    tmp = sorted(input().rstrip().split(','))
    
    for t in tmp :
        if t in board.keys() :
            if board[t]:
                board[t] = 0
                res -= 1
    print(res)
    