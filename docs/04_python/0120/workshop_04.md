# Workshop_04

1. **숫자의 의미**

> 정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.
>
> ```
> get_secret_word([83,115,65,102,89])
> ```



``` python
def get_secret_word(lst):
    words = str()
    print(words)
    for word in lst :
        words += chr(word)
    return words

print(get_secret_word([83,115,65,102,89]))
```





---



2. **내 이름은 몇일까?**

> 문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~~Z, a~~z로만 구성되어 있다.
>
> ```python
> get_secret_number('tom') #=> 336
> ```



``` python
def get_secret_number(name):
    #총합 변수 초기화
    total = 0
    #반복문( 숫자의 합 ))
    for n in name:
    #문자를 -> 10진수
    #총합변수 += 10진수값 
        total += ord(n)
    #반환
    return total
get_secret_number('tom')
```





---



3.  강한 이름

> 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.
>
> ```python
> get_strong_word('z','a') # => 'z'
> get_strong_word('tom','john') #=> 'john'
> ```



``` python
def get_strong_word(name_a,name_b):
    #총합 변수 a,b 초기화
    total_a = total_b = 0
    #name_a 반복문 ( 숫자의 합 )
    #문자 -> 십진수 & 총합변수에 += 10진수값
    for a in name_a:
        total_a+=ord(a)
    #name_b 반복문 ( 숫자의 합 )
    #문자 -> 십진수 & 총합변수에 += 10진수값
    for b in name_b:
        total_b+=ord(b)
    #if 조건문 비교하여서 큰갑 리턴
    return name_a if total_a > total_b else name_b 

print(get_strong_word('z','a'))# => 'z'
print(get_strong_word('tom','john')) #=> 'john'
```