# 10994_별 찍기
# 2022-08-13

def DFS(N, idx):
    if N == 1:
        arr[idx][idx] = "*"
        return

    length = 4 * N - 3

    for  i in range(idx, idx + length):
        arr[idx][i] = "*"
        arr[idx+length-1][i] = "*"

        arr[i][idx] = "*"
        arr[i][idx+length-1] = "*"

    return DFS(N-1, idx+2)

N = int(input())
lens = 4 * N - 3

arr = [[" "] * lens for _ in range(lens)]

DFS(N, 0)

for i in range(lens):
    for j in range(lens):
        print(arr[i][j], end="")
    print()