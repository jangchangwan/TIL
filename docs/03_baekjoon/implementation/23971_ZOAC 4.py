H, W, N, M = map(int, input().split())

row, col = 0, 0

if  H % (N + 1):
    col = H // (N + 1) + 1
else:
    col = H // (N + 1)
    
if  W % (M + 1):
    row = W // (M + 1) + 1
else:
    row = W // (M + 1)
print(row * col)