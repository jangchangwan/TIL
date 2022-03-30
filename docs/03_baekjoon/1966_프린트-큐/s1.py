# 1966_프린트-큐-문제풀이
# 2022-03-27


T = int(input())

for tc in range(1, T+1):
    # 문서 수
    N, M = map(int, input().split())

    import_lst = list(map(int, input().split()))
    index = 0
    front = -1
    rear = 0
    queue = import_lst
    cnt = 1
    length = N
    while front != rear:
        front += 1

        temp = queue[front]
        temp_cnt = 0
        for i in queue[front:]:
            if temp < i:
                queue.append(temp)
                rear += 1
                break
            temp_cnt += 1
        # 뒤에 자신보다 중요도가 높은 숫자가 없을 경우
        if temp_cnt == length:
            if index == M:
                break
            length -= 1
            cnt += 1

        index = (index + 1) % N




    print(cnt)