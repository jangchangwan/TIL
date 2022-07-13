# 1135_뉴스전하기
# 2022-07-07

'''
회사는 트리구조
모든 직원은 직속 상사가 1명만 존재

민석이는 회사 매니저 : 루트
민석이가 직속 부하에게 한번에 한사람씩 전화를 건다
직속 부하에게만 전화 가능
전화는 1분
모든 직원에게 소식을 돌리는데 걸리는 최소시간
'''


def DFS(node):
    visited = []

    for v in Tree[node]:
        visited.append(DFS(v))
    # 회사에 부하직원이 없는 경우
    if not visited:
        return 0
    visited.sort(reverse=True)
    ans = 0
    for i in range(len(visited)):
        ans = max(ans, visited[i] + i + 1)
    return ans


# 입력
N = int(input())
N_lst = list(map(int, input().split()))


# 트리구조 생성
Tree = [[] for _ in range(N)]
for i in range(1, N):
    Tree[N_lst[i]].append(i)

answer = DFS(0)
print(answer)