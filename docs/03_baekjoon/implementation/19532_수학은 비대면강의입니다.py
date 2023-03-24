
def solution():
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            temp = a * i + b * j
            temp2 = d * i + e * j
            if temp == c and temp2 == f:
                return i , j
            


a, b, c, d, e, f = map(int, input().split())
x, y = solution()
print(x, y)