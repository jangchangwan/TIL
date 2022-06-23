# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.


#print(snail_data)
def snail_day(data):
    snail_data = list(map(int,data.split()))
    day_data = (snail_data[2]-snail_data[0])//(snail_data[0]-snail_data[1])
    # print('day_data : ',day_data)
    abc_data = snail_data[2]-(day_data*(snail_data[0]-snail_data[1]))
    # print('abc_data : ',abc_data)
    result = 0

    
    while result < abc_data:
        day_data += 1
        result += snail_data[0]
        if result >= abc_data:
            return day_data
        else :
            result-=snail_data[1]
    return day_data

a = input()
print(snail_day(a))