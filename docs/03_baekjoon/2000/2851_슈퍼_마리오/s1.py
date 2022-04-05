import sys
sys.stdin = open('input.txt', 'r')


stack = []
for i in range(10):
    num = int(input())

    if len(stack) == 0:
        stack.append(num)
    elif stack[-1] < 100:
        num += stack[-1]
        stack.append(num)
    elif stack[-1] >= 100:
        num_a = stack.pop()
        if (100 - stack[-1]) >= (num_a - 100):
            stack.append(num_a)
        break
print(stack[-1])