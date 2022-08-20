# 4589_Gnome Sequencing
# 2022-08-20


T = int(input())

print("Gnomes:")
for tc in range(T):
    gnomes = list(map(int, input().split()))

    temp_1 = sorted(gnomes)
    temp_2 = temp_1[::-1]

    if gnomes == temp_1 or gnomes == temp_2:
        print("Ordered")
    else:
        print("Unordered")