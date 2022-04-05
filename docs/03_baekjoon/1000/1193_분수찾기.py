# 1 3 6 10 15 21
#  2 3 4  5  6


N = int(input())

i = 1
n = 1
num = 1

if N == 1:
    print('1/1')
else :
    while N >= num:
        num += n*i
        i += 1
        
    # print(i,num)
    if i % 2 == 0:
        print('{}/{}'.format(num-N,i-(num-N)))
    else:
        print('{}/{}'.format(i-(num-N),num-N))
