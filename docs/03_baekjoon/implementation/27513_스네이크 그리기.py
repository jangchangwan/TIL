# 스네이크

N, M = map(int, input().split())

# 둘중 하나가 짝수일 경우
if (N % 2 == 0 or M % 2 == 0 ):
    print(f"{N*M}")
    # y가 홀수일 경우
    if ( M % 2 == 1):
        for i in range(1, M+1):
            print(f"1 {i}")
        for j in range(0, M-3, 2):
            for i in range(2,N+1):
                print(f"{i} {M-j}")
            for i in range(N, 1, -1):
                print(f"{i} {M-j-1}")
        for i in range(2, N+1):
            print(f"{i} 3")
        
        for i in range(0, N-1, 2):

            print(f"{N-i} 2")
            print(f"{N-i} {1}")

            if (N-i-1 != 1):
                print(f"{N-i-1} 1")
                print(f"{N-i-1} 2")
    
    else:
        for i in range(1, M+1):
            print(f"1 {i}")
        for j in range(0, M, 2):
            for i in range(2, N+1):
                print(f"{i} {M-j}")
            for i in range(N, 1, -1):
                if (M-j-1 != 0):
                    print(f"{i} {M-j-1}")
# 둘다 홀수일 경우
else:
    print(f"{N*M-1}")
    for i in range(2, M+1):
        print(f"1 {i}")
    
    for j in range(0, M-3, 2):
        for i in range(2, N+1):
            print(f"{i} {M-j}")
        for i in range(N, 1, -1):

            print(f"{i} {M-j-1}")
    
    for i in range(2, N+1):
        print(f"{i} {3}")
    
    for i in range(0, N-1, 2):
        print(f"{N-i} {2}")
        print(f"{N-i} {1}")
        print(f"{N-i-1} {1}")
        print(f"{N-i-1} {2}")