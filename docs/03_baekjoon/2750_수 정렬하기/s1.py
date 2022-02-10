T = int(input())

num_list = list()
for t in range(T):
    n = int(input())
    num_list.append((n))


for i in range(len(num_list)-1, 0, -1):
    for j in range(i):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for num in num_list:
    print(num)
