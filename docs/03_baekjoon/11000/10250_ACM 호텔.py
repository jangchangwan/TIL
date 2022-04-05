T = int(input())

for t in range(T):
    hotel_data = list(map(int,input().split()))

    H = hotel_data[2] % hotel_data[0]
    W = (hotel_data[2] // hotel_data[0]) +1
    if hotel_data[2] % hotel_data[0] ==0:
        W = (hotel_data[2] // hotel_data[0])
        H = hotel_data[0]
    print(H*100+W)