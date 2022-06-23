# 1120_문자열
# 2022-06-21


A, B = input().split()

answer = len(A)

for i in range(len(B)-len(A)+1):

    cnt = 0
    temp = B[i:i+len(A)]

    for j in range(len(A)):
        if A[j] == temp[j]:
            cnt += 1

    answer = min(answer, len(A)-cnt)

print(answer)