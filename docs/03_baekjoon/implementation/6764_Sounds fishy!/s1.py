# Sounds fishy!
# 2022-08-24

number_list = list(int(input()) for _ in range(4))


diff = []
for i in range(3):
    temp = number_list[i+1] - number_list[i]
    diff.append(temp)

sign = [0, 0, 0]
for d in diff:
    if d > 0:
        sign[0] += 1
    elif d == 0:
        sign[1] += 1
    elif d < 0:
        sign[2] += 1

if sign[0] == 3:
    print("Fish Rising")
elif sign[1] == 3:
    print("Fish At Constant Depth")
elif sign[2] == 3:
    print("Fish Diving")
else:
    print("No Fish")

