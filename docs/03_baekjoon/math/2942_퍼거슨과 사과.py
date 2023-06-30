def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

  
def GAD(num):
    divisors = list()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
              divisors.append(i)
              if ((i**2) != num) : 
                divisors.append(num // i)
    divisors.sort()
    return divisors


A, B = map(int, input().split())

num_list = GAD(GCD(A, B))

for num in num_list:
    print(f"{num} {A//num} {B//num}")