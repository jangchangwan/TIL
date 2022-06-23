D, H, W = map(int, input().split())

r =(H**2 + W **2) **0.5

print(int(D*H/r), int(D*W/r))