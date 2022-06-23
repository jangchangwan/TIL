# 23037_5의 수난_문제풀이
# 2022-06-05


# 다섯제곱해주는 함수
def five_squared(n):
    return n**5


# 정수는 반복문을 쓸수없으므로 문자열로 데이터 받는다.
number = input()

# 결과 변수 생성
ans = 0

# 반복
for num in number:
    # 연산을 위해 정수로 변환
    ans += five_squared(int(num))

# 출력
print(ans)