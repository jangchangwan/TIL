# 이중 우선순위 큐
# 2022-07-09

import heapq

T = int(input())

for tc in range(T):
    K = int(input())
    max_heaq, min_heaq = [], []
    visited = [0] * K

    for idx in range(K):
        comment, number = input().split()

        if comment == 'I':
            heapq.heappush(min_heaq, (int(number), idx))
            heapq.heappush(max_heaq, (-int(number), idx))
            visited[idx] = 1

        elif comment == 'D':
            if number == '1':
                while max_heaq and not visited[max_heaq[0][1]]:
                    heapq.heappop(max_heaq)
                if max_heaq:
                    visited[max_heaq[0][1]] = 0
                    heapq.heappop(max_heaq)
            else:
                while min_heaq and not visited[min_heaq[0][1]]:
                    heapq.heappop(min_heaq)
                if min_heaq:
                    visited[min_heaq[0][1]] = 0
                    heapq.heappop(min_heaq)

    while min_heaq and not visited[min_heaq[0][1]]:
        heapq.heappop(min_heaq)
    while max_heaq and not visited[max_heaq[0][1]]:
        heapq.heappop(max_heaq)


    if not min_heaq or not max_heaq:
        print('EMPTY')
    else:
        max_number = -max_heaq[0][0]
        min_number = min_heaq[0][0]
        print(max_number, min_number)
