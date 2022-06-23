# 14720

'''
맨처음 딸기 -> 초코 -> 바나나 -> 딸기
뒤로 갈수없고 쭉직진으로 갈 때
영학이가 마실수있는 우유의 수
'''

N = int(input())

N_lst = list(map(int, input().split()))

cnt = 0

for i in range(len(N_lst)):
    if cnt % 3 == N_lst[i]:
        cnt += 1
print(cnt)