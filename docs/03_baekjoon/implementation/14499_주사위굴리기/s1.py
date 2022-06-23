import sys
sys.stdin = open('input.txt', 'r')

N, M, start_r, start_c, command = map(int, input().split())

arr = [[0] * M for _ in range(N)]
temp = []
for i in range(N):
    a = list(map(int, input().split()))
    temp.extend(a)

num = 0
for j in range(M):
    for i in range(N):
        arr[i][j] = temp[num]
        num += 1

print(arr)
command_lst = list(map(int, input().split()))
print(command_lst)