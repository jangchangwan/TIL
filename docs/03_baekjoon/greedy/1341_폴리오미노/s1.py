# 1343_폴리오미노
# 2022-06-11

board = input()

idx = 0
res = ''
while idx < len(board):

    if board[idx:idx + 4] == 'XXXX':
        res += 'AAAA'
        idx += 4
    elif board[idx:idx + 2] == 'XX':
        res += 'BB'
        idx += 2
    elif board[idx] == '.':
        res += '.'
        idx += 1
    else:
        break

if len(board) == len(res):
    print(res)
else:
    print(-1)