"""
섞여있는 공 리스트를  색깔을 분리 할려고한다
1. 다른 공들은 한번에 점프할 수 있다.
2. 옮길공을 선택하면 그색깔 공만 옮길 수 있다.

최소이동횟수를 구해라
"""


N = int(input())
ball_list = input()

red = ball_list.count('R')
blue = N - red
answer = N

type_A = ball_list.rstrip("R")
answer = min(answer, red - (N - len(type_A)))

type_B = ball_list.rstrip("B")
answer = min(answer, blue - (N - len(type_B)))

type_C = ball_list.lstrip("R")
answer = min(answer, red - (N - len(type_C)))

type_D = ball_list.lstrip("B")
answer = min(answer, blue - (N - len(type_D)))

print(answer)