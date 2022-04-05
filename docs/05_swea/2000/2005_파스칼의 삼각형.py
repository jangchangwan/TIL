# 크기가 N인 파스칼의 삼각형을 만들어야 한다.
# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
# 1. 첫 번째 줄은 항상 숫자 1이다.
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
# N이 4일 경우,
# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
def pascal_rec(num):
    if num == 0:
        return []
    elif num == 1:
        return [1]
    else:
        # 처음 
        new_list = [1]
        last_list = pascal_rec(num-1)
        # 중간값
        for i in range(len(last_list)-1):
 
            new_list.append(last_list[i] + last_list[i+1])
        new_list += [1]
    return new_list

T = int(input())

for t in range(1,T+1):
    print(f'#{t}')
    num = int(input())
    for i in range(1,num+1):
        for j in pascal_rec(i):
            print(j, end=' ')
        print()