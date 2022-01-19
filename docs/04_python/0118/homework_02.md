# homework_02

1.  **Mutable & Immutable**

> 주어진 컨테이너들을 각각 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

``` python
String, List, Tuple, Range, Set, Dictionary
```



``` python
# 변경 가능한 것 (mutable) : List , Set , Dictionary
# 변경 불가능한 것 (immutable) : String , Tuple , Range
```



``` python
# Set, Dictionary 는 순서가 없을뿐 변경가능하다 
```





---

2. **홀수만 담기**

> range 와 slicing 을 활용하여 1부터 50까지의 숫자 중 홀수로만 이루어진 리스트를 만드시오.



``` python
list(range(1,51)[::2])

# list() : ()안에 데이터를 리스트 화
# range(n,m,s) : n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스
# [::k] : k 간격으로 slicing
```





---

3. **Dictionary 만들기**

> 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.



``` python
student = { 김나라 : 29 , 장소유 : 26 , 권주식 : 29 , 이미소 : 30 }
```



``` python
# dictionary 구조 : key 와 value로 이루어져 있다.
# key는 immutable 한 데이터만 사용 가능 ex) string, integer, float, boolean, tuple, Range
# value는 모든 값을 사용 가능
```





---

4. **반복문으로 네모 출력**

> 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

``` python
n = 5
m = 9
```



``` python
# 변수 초기화
n , m = 5, 9
# 반복문
for i in range(1,m+1) : # 세로 설정
    print(n*'*') # 가로 출력
```



``` python
# range() : 시작값은 0 , 간격은 1이 초기값이므로 필요시 수정해야함
# 문자열 에 곱연산시  : n번 반복출력된다.
```





---

5. **조건 표현식**

> 주어진 코드의 조건물을 조건 표현식으로 바꾸어 작성하시오.

``` python
temp = 36.5
if temp >= 37.5:
    print('입실 불가')
else:
    print('입실 가능')
```



``` python
temp = 36.5
print('입실 불가') if temp >= 37.5  else print('입실 가능')
```



``` python
# 조건 표현식 기본 양식 : <True인 경우 명령> if < 조건 > else <False 인 경우 명령>
```





---

6. **평균 구하기**

> 주어진 list에 담긴 숫자들의 평균값을 출력하시오.

``` python
scores = [80, 89, 99, 83]
```



``` python
scores = [80, 89, 99, 83]
# 변수 초기화
count = total = 0
# 반복문 
for score in scores :
    total += score # 총합 
    count += 1 # 개수
print(total/count)
```