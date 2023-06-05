'''
문제
세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수, C는 109보다 작거나 같은 음이 아닌 정수이다. 둘째 줄에 물건의 무게가 주어진다. 무게도 109보다 작거나 같은 자연수이다.

출력
첫째 줄에 가방에 넣는 방법의 수를 출력한다.

예제 입력 1 
2 1
1 1
예제 출력 1 
3
'''

def bf(arr,seq,idx,summ):
    if len(arr) == idx:
        seq.append(summ)
        return seq
    
    bf(arr,seq,idx+1,summ)
    bf(arr,seq,idx+1,summ+arr[idx])
    
    return seq

N, C = map(int, input().split())
items = list(map(int, input().split()))

item1, item2 = items[:N//2], items[N//2:]
left_item, rigth_item = list(), list()


# 절반씩 탐색
left_item = bf(item1 , left_item, 0, 0)
rigth_item = sorted(bf(item2 , rigth_item, 0, 0))
result = 0

for i in left_item:
    if C - i < 0:
        continue
    
    # 이분 탐색
    start,end = 0,len(rigth_item)
    while(start < end):
        mid = (start + end)//2
        if rigth_item[mid] <= C - i:
            start = mid + 1
        else:
            end = mid
    result += start
print(result)