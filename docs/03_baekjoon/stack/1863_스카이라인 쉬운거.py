N = int(input())

stack = []
result = 0


for _ in range(N):
    r, c = map(int, input().split())
    
    while len(stack) > 0 and stack[-1] > c:
        result += 1
        stack.pop()
    
    if len(stack) > 0 and stack[-1] == c:
        continue
    
    stack.append(c)

while len(stack)>0:
    if stack[-1] >0:
        result += 1
    stack.pop()

print(result)