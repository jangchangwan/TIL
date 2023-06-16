"""
상하좌우로 1~9 숫자가 하나씩 적혀있다 (중복 O)

시계수 : 시계방향으로 숫자를 읽었을때 나오는 수중 가장 작은 수

수를 주어졌을때 시계수는 몇번째 시계수인지 구하여라

"""

def find_min_value(i, j, k, h):
    value = []
    value.append(i*1000 + j*100 + k*10 + h)
    value.append(j*1000 + k*100 + h*10 + i)
    value.append(k*1000 + h*100 + i*10 + j)
    value.append(h*1000 + i*100 + j*10 + k)
    value.sort()
    return value[0]


num_set = set()
num_set.add(0)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for h in range(1, 10):
                value = find_min_value(i, j, k, h)
                num_set.add(value)
                
result = sorted(list(num_set))

a,b,c,d = map(int, input().split())

number = find_min_value(a, b, c, d)
idx = 0
answer = -1
for r in result:
    if number == r :
        answer = idx
        break
    idx += 1
    
print(answer)