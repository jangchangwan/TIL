# 문제
# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 
# 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

# 입력
# 첫째 줄에 두 정수 min과 max가 주어진다.

# 출력
# 첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

# 제한
# 1 ≤ min ≤ 1,000,000,000,000
# min ≤ max ≤ min + 1,000,000
# 예제 입력 1 
# 1 10
# 예제 출력 1 
# 7



min, max = map(int, input().split())

answer = max - min + 1
check = [False] * (max-min+1)

for i in range(2, int(max**0.5+1)):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):
        if not check[j-min] :
            check[j-min] = True
            answer -= 1
print(answer)