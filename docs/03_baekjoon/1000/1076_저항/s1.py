import sys
sys.stdin = open('input.txt', 'r')


data = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

input_lst = []
for _ in range(3):
    temp = input()
    input_lst.append(temp)
ans = 0
for i in range(3):
    if i == 0:
        ans += data[input_lst[i]] * 10
    elif i == 1:
        ans += data[input_lst[i]]
    else:
        ans *= 10**data[input_lst[i]]
print(ans)