N = int(input())

data = [0, 0]
for _ in range(N):
    score = input()
    if score == "D":
        data[0] += 1
    else:
        data[1] += 1
         
    dis = data[0] - data[1]
    if dis <= -2 or dis >= 2:
        break
print(f'{data[0]}:{data[1]}')