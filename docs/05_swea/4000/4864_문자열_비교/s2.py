import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T+1):

    str1 = list(input())
    str2 = list(input())
    # 같으면 두번째 반복문 끝내고 첫번째 반복문으로 넘어감

    cnt = 0
    i = j = 0
    index = 1
    while cnt < len(str1) and j < len(str2) :
        # 만약 문자가 같다면, i와 j를 다음 인덱스로 넘긴다

        if str1[i] == str2[j]:
            i += 1
            j += 1
            cnt += 1
        else:
            i = 0
            j = index
            cnt = 0
            index += 1

    print(cnt)


    if cnt == len(str1):
        print("#{} 1" .format(t))
    else:
        print("#{} 0" .format(t))