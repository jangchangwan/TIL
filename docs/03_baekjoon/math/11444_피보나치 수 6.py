import sys
input=sys.stdin.readline

p=1000000007

def power(arr, n):
    if n == 1:
        return arr
    elif n % 2:
        return multi(power(arr, n-1),arr)
    else:
        return power(multi(arr, arr), n // 2)
      
#행렬의 곱셈
def multi(a, b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % p
    return temp
#초기 행렬

arr=[[1,1],[1,0]]

#피보나치 초기값
start=[[1],[1]]
N = int(input())
if N < 3:
    print(1)
else:
    print(multi(power(arr, N - 2),start)[0][0])

