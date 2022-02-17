def my_sort(num):
    for i in range(len(num)-1):
        min_idx = i
        for j in range(i+1, len(num)):
            if num[j] < num[min_idx]:
                min_idx = j

        num[i], num[min_idx] = num[min_idx], num[i]

my_list = [5,4,3,2,1]
my_sort(my_list)
print(my_list)