# 문제
# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

# 출력
# 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 3
# 6
# 20
# 100
# 예제 출력 1 
# 7
# 23
# 101

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
           return False
    return True
 

T = int(input())

for tc in range(T):
    N = int(input())
    while True:
        if is_prime(N):
            print(N)
            break
        else:
            N += 1
