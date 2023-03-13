# 3×3 표에 다음과 같이 수가 채워져 있다. 오른쪽 아래 가장 끝 칸은 비어 있는 칸이다.

# 1	2	3
# 4	5	6
# 7	8	 
# 어떤 수와 인접해 있는 네 개의 칸 중에 하나가 비어 있으면, 수를 그 칸으로 이동시킬 수가 있다. 
# 물론 표 바깥으로 나가는 경우는 불가능하다. 우리의 목표는 초기 상태가 주어졌을 때, 최소의 이동으로 위와 같은 정리된 상태를 만드는 것이다. 다음의 예를 보자.

# 1	 	3
# 4	2	5
# 7	8	6
# 1	2	3
# 4	 	5
# 7	8	6
# 1	2	3
# 4	5	 
# 7	8	6
# 1	2	3
# 4	5	6
# 7	8	 
# 가장 윗 상태에서 세 번의 이동을 통해 정리된 상태를 만들 수 있다. 이와 같이 최소 이동 횟수를 구하는 프로그램을 작성하시오.

# 입력
# 세 줄에 걸쳐서 표에 채워져 있는 아홉 개의 수가 주어진다. 한 줄에 세 개의 수가 주어지며, 빈 칸은 0으로 나타낸다.

# 출력
# 첫째 줄에 최소의 이동 횟수를 출력한다. 이동이 불가능한 경우 -1을 출력한다.

# 예제 입력 1 
# 1 0 3
# 4 2 5
# 7 8 6
# 예제 출력 1 
# 3


# 함수
def BFS():
    global visited
    queue = list([puzzle])
    
    front = -1
    rear = 0

    while front != rear:
        front += 1
        now = queue[front]
        zero = now.index('0') # 0 위치

        cnt = visited[now]
        
        # 찾았을 경우
        if now == "123456780":
            return cnt
        
        r = zero // 3
        c = zero % 3
        cnt += 1
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < 3) and (0 <= nc < 3):
                nz = nr * 3 + nc
                puzzle_lst = list(now)
                puzzle_lst[zero], puzzle_lst[nz] = puzzle_lst[nz], puzzle_lst[zero]
                nn = ""
                for item in puzzle_lst:
                    nn += item
                if visited.get(nn, 0) == 0:
                    visited[nn] = cnt 
                    queue.append(nn)   
                    rear += 1

    # 못찾을 경우
    return -1


# 입력
puzzle = ""
for i in range(3):
    temp = list(input().split())
    for t in temp:
        puzzle += t

# 변수 초기화
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited ={ puzzle : 0 }
# 실행
answer = BFS()

# 출력
print(answer)