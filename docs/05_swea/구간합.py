T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    num_list = list(map(int,input().split()))
    # print("M,N 값 출력 : ",M,N)
    # print("num_list : ",num_list)
    # 최대값 최소값 변수 설정
    max_result = 0
    min_result = 10000*M

    # 값을 N개 더해주고 리스트 만들기
    for idx in range(0,N-M+1,1):
        sum_num = 0
        # 구간합 구하기
        for n in range(idx,idx+M):
            sum_num += num_list[n]
        # 구간합이 max보다 클경우 max값 변경
        print("구간합 :",sum_num)
        if sum_num > max_result:
            max_result = sum_num
        # 구간합이 min보다 작을경우
        if sum_num < min_result:
            min_result = sum_num
    
    # 차이값을 구하기
    print('#{} {}'.format(t,max_result-min_result))