four = [int(input()) for _ in range(4)]
two = [int(input()) for _ in range(2)]

four.sort()
two.sort()

print(sum(four[1:])+two[1])