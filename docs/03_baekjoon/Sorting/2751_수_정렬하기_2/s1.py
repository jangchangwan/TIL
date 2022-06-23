import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
num_list = list()
for t in range(T):
    num_list.append(int(input()))

num_list.sort()

for num in num_list:
    print(num)