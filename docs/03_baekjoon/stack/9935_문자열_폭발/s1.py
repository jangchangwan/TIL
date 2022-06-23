# 9935_문자열_폭발_문제풀이
# 2022-04-25

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
text = input().rstrip()
bang = list(map(str, input().rstrip()))
stack = []




for t in text:
    stack.append(t)
    # 폭발할경우
    if t == bang[-1] and stack[-len(bang):] == bang:
        # 스택에서 폭발 길이만큼 pop을 한다
        for _ in range(len(bang)): stack.pop()

'''
ans 를 for문으로 stack의 값을 하나씩 더해줄 경우
2%에서 시간초과가 발생한다.
join 메소드가 for문인 O(n) 시간복잡도보다 더 동작이 짧은것같다
'''

# ans = ''
# for s in stack:
#     ans += s
#
# if ans:
#     print(ans)
# else:
#     print('FRULA')


if len(stack):
    print(''.join(stack))
else:
    print('FRULA')