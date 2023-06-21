"""
꼭지점 3개의 문자열이 같을 경우 보상을준다

만족하는 문자열이 없는 경우 LOOOOOOOOSER! 출력
N 범위는 12
N = 4
   a
  b c
 c d d
a d c a

정답 ac

N = 6
     a
    z d
   e f c
  c r h i
 j r r m z
n z o c p q
      
정답 crz



1 3 1 4

1 2 3 4
  5   6
  7   8
      9
"""



while True:
    N = int(input())
    if N == 0:
        break
    
    else:
        word = list(input())
        print(word)
