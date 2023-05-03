"""
문제
길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.

입력
첫 번째 줄에는 수열의 길이 N이 주어진다. (1 ≤ N ≤ 100,000)

두 번째 줄에는 수열을 나타내는 N개의 정수가 주어진다. 수열에 나타나는 수는 모두 1 이상 100,000 이하이다.

출력
조건을 만족하는 경우의 수를 출력한다.

예제 입력 1 
5
1 2 3 4 5
예제 출력 1 
15
"""

# 시간초과

N = int(input())
arr = list(map(int, input().split()))


start, end = 0, 1
count = 0

while start != N:
    check_list = arr[start:end]
    check_set = set(check_list)
    
    if len(check_list) == len(check_set):
        count += 1
    
    start += 1
    if start != N and start == end:
        start = 0
        end += 1

print(count)
    
    
    
# 성공
import sys

input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().split()))

start, end = 0, 0
count = 0
seq = [False for _ in range(1000001)]

while start < N and end < N:
    if not seq[arr[end]]:
        seq[arr[end]] = True
        end += 1
        count += (end - start)
    else:
        seq[arr[start]] = False
        start += 1

print(count)