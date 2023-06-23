# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.


# 입력 예시
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# 출력 예시
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%


# 평균을 구해서
# 평균 이상만 카운팅해서
# 평균 이상 사람 수 / 총 사람 수
def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

C = int(input())

for c in range(C):
    scores = list(map(int,input().split()))

    total = 0
    total_cnt = 0
    
    for score in scores[1:] :
        total += score
    ave_score = total / scores[0]
    for score in scores[1:] :
        if score > ave_score:
            total_cnt += 1
    
    print('{:.3f}%'.format(roundTraditional(total_cnt/scores[0]*100,3)))


    