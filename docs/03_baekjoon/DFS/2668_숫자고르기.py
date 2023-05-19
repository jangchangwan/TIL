# dfs 정의
def dfs(first, second, num):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:
        if first == second:
            answer.update(first)
            return True
        return False
    return dfs(first, second, arr[num])


N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
answer = set()



# dfs 실행
for i in range(1, N+1):
    if i not in answer:
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')