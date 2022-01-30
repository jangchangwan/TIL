#테스트 케이스
T = int(input())
for t in range(T):
    data = input()


    number, alphabat = data.split()
    #print(number, alphabat)
    result = ''
    for alpha in alphabat:
        result += (alpha*int(number))

    print(result)

