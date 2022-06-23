# 6550_부분문자열
# 2022-06-20


while True:
    try:
        A, B = input().split()

        idx = 0
        flag = False

        for i in range(len(B)):
            if B[i] == A[idx]:
                idx += 1
                if idx == len(A):
                    flag = True
                    break

        if flag:
            print('Yes')
        else:
            print('No')

    except:
        break