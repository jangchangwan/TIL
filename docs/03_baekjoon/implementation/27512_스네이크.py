

# 입력
# 두 정수 n과 m이 한 줄에 공백으로 분리되어 주어집니다.

# 출력
# 문제의 정답을 출력하세요.

# 예제 입력 1 
# 2 2
# 예제 출력 1 
# 4


N, M = map(int, input().split())

result = N * M
if ( N * M % 2 ): 
    print(result - 1)
else: 
    print(result)