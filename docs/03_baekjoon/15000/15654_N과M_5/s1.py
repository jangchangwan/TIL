# 15654_N과M_5_문제풀이
# 2022-04-13


'''
    백트래킹으로 순열구하는 문제
    방문 리스트를 만들어서 없을경우만 동작하여
    M 만큼 반복한후 출력하게 만든다
'''
import sys
sys.stdin = open('input.txt', 'r')


def DFS(arr, visited, cnt):
    if cnt == 0:
        print(*visited)
        return
    for num in arr:

        if num not in visited:
            visited.append(num)
            DFS(arr, visited, cnt - 1)
            visited.pop()


N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
N_lst.sort()
DFS(N_lst, [], M)