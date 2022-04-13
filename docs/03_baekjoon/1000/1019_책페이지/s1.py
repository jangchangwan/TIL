# 1019_책페이지_문제풀이
# 2022-04-12

'''
10으로 나눠서 나머지를 해당 값에 넣어준다
299 인경우 200 ~ 299 가 앞아지 2가 총 99번 나오므로 굳이 2를 99번탐색할 이유가없다.

'''
import sys
sys.stdin = open('input.txt','r')



def cal(x, ans, point):
    while x > 0:
        ans[x % 10] += point
        x //= 10


end = int(input())
# 배수
k = 1
# 시작
start = 1
ans = [0] * 10

while start <= end:
    while end % 10 != 9:
        cal(end, ans, k)
        end -= 1
    if end < start:
        break
    while start % 10 != 0:
        cal(start, ans, k)
        start += 1
    start //= 10
    end //= 10
    for i in range(10):
        ans[i] += (end - start + 1) * k
    k *= 10

# 출력부
print(*ans)
