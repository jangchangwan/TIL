'''

1 2     4
2 2*2-1 9
3 3*2-1     25
4 9 81

N (N-1)*2^2

'''


N = int(input())

temp = [0, 2]
answer = [0, 4]

for i in range(2, 17):
    base = temp[i-1] * 2 - 1
    temp.append(base)
    answer.append(int(base*base))
    
print(answer[N+1])
