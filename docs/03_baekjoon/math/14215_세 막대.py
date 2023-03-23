

length_list = list(map(int, input().split()))
length_list.sort()

result = length_list[0] + length_list[1] + min(length_list[2], length_list[0] + length_list[1] - 1)
print(result)

