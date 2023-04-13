N = int(input())
N_list = list(map(int, input().split()))

result = [0] * N

for i in range(1,N+1):
    temp = N_list[i-1]
    count = 0
    
    for j in range(N):
        if count == temp and result[j] == 0:
            result[j] = i
            break
        elif result[j] == 0:
            count += 1 
print(*result)
