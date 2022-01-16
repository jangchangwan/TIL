# 입출력과 사칙연산



1. 고양이 출력

```python
print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \\(__)|')
```

- `\\ ` : print 함수 내에서 ' \ '를 출력한다.

- `''` : ''(큰따옴표) 를 출력하고 싶은 경우 사용 

  - 반대의 경우도 성립 

    

2.  강아지 출력

``` python
print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')
```



3. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

``` python
nums = input()
list_nums = nums.split(' ') 
print(int(list_nums[0])+int(list_nums[1]))
```

- `문자열.split('구분자')` : 문자열를 분리할때 사용

  

4. 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오

```  python
nums = input()
list_nums = nums.split(' ')
print(int(list_nums[0])-int(list_nums[1]))
```



5. 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

``` python
nums = input()
list_nums = nums.split(' ')
a = int(list_nums[0]) / int(list_nums[1])
#a = round(a, 9)
print('{:.9f}'.format(a))
```

- `round( 값, 표기하고싶은 자릿수)` : 반올림할경우 사용



6. 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

``` python
nums = input()
y = nums.split(' ')
a = int(y[0])
b = int(y[1])
sum = a+b
sub = a-b
mul = a*b
quo = a//b
rem = a%b
print(sum)
print(sub)
print(mul)
print(quo)
print(rem)
```

7. (A+B)%C는 ((A%C) + (B%C))%C 와 같을까? , (A×B)%C는 ((A%C) × (B%C))%C 와 같을까? 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

``` python
nums = input()
nums = nums.split(' ')
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print((a%c)*(b%c)%c)
```



8. (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

​	(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값	을 구하는 프로그램을 작성하시오

``` python
num_1 = int(input())
num_2 = int(input())
list_2 = []
while (num_2!=0):
    list_2.append(num_2%10)
    num_2 = num_2 // 10
result_1 = num_1 * int(list_2[0])
result_2 = num_1 * int(list_2[1])
result_3 = num_1 * int(list_2[2])
print(result_1)
print(result_2)
print(result_3)
print(result_1+result_2*10+result_3*100)
```

