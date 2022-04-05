
T = int(input())

for t in range(T):
    x,y= map(int,input().split())

    distance = y-x
    cnt = 0
    move = 1
    move_now = 0
    
    while move_now < distance:
        cnt += 1
        move_now += move
        if cnt % 2 == 0:
            move += 1
    print(cnt) 
# 10
# 1 2 3 2 1 1
# # 



