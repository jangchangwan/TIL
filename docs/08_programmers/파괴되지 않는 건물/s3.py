def solution(board, skill):
    n = len(board)
    m = len(board[0])
    answer = 0
    skill_collect = [[0] * (m + 1) for _ in range(n + 1)]
    for s in skill:
        t, x1, y1, x2, y2, degree = s

        if t == 1:
            degree = -degree

        skill_collect[x1][y1] += degree
        skill_collect[x1][y2 + 1] -= degree
        skill_collect[x2 + 1][y1] -= degree
        skill_collect[x2 + 1][y2 + 1] += degree


    print(skill_collect)
    for i in range(n):
        for j in range(m):
            skill_collect[i][j + 1] = skill_collect[i][j] + skill_collect[i][j + 1]

    for i in range(m):
        for j in range(n):
            skill_collect[j + 1][i] = skill_collect[j][i] + skill_collect[j + 1][i]

    for i in range(n):
        for j in range(m):
            skill_collect[i][j] = skill_collect[i][j] + board[i][j]
            if skill_collect[i][j] > 0:
                answer += 1
    return answer


print(
    solution(
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]],
    )
)