import sys
sys.stdin = open('input.txt', 'r')

N, data = map(int, sys.stdin.readline().split())

num_list = list()
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)
num = num_list[::-1]
cnt = 0
for i in num:
    cnt += data//i
    data %= i
    
print(cnt)