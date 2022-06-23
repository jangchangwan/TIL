def Fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)


number = int(input())
print(Fibonacci(number))
