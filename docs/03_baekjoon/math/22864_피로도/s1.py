# 22864_피로도_문제풀이
# 2022-04-29

A, B = map(str, input().split())

min_A = ''
max_A = ''
min_B = ''
max_B = ''

for a in A:
    if a == '5' or a == '6':
        min_A += '5'
        max_A += '6'
    else:
        min_A += a
        max_A += a

for b in B:
    if b == '5' or b == '6':
        min_B += '5'
        max_B += '6'
    else:
        min_B += b
        max_B += b

print(int(min_A)+int(min_B), int(max_A) + int(max_B))