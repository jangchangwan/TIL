# 2022 KAKAO BLIND RECRUITMENT 파괴되지 않는 건물
# 2022-05-14

# 누적합
# 정확성 성공 / 효율성 성공
from pprint import pprint

def solution(board, skill):
    answer = 0
    row = len(board)
    col = len(board[0])
    temp = [[0] * (col + 1) for _ in range(row + 1)]

    for type, r1, c1, r2, c2, damage in skill:
        if type == 1:
            temp[r1][c1] -= damage
            temp[r1][c2 + 1] += damage
            temp[r2 + 1][c1] += damage
            temp[r2 + 1][c2 + 1] -= damage
        else:
            temp[r1][c1] += damage
            temp[r1][c2 + 1] -= damage
            temp[r2 + 1][c1] -= damage
            temp[r2 + 1][c2 + 1] += damage


    # 행 기준 누적합
    for i in range(row):
        for j in range(col):
            temp[i][j + 1] += temp[i][j]

    # 열 누적합
    for i in range(col):
        for j in range(row):
            temp[j + 1][i] += temp[j][i]


    # 기존 배열과 합함
    for i in range(row):
        for j in range(col):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
               [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

print(solution([[1,2,3],[4,5,6],[7,8,9]],
               [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
