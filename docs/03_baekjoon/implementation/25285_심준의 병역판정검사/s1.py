# 심준의 병역판점겅사
# 2022-06-10


def check(cm, bmi):
    if cm < 140.1:
        return 6
    elif 140 <= cm < 146:
        return 5
    elif 146 <= cm < 159:
        return 4
    elif 159 <= cm < 161:
        if 16 <= bmi < 35:
            return 3
        else:
            return 4
    elif 161 <= cm < 204:
        if 20 <= bmi < 25:
            return 1
        if 18.5 <= bmi < 20 or 25 <= bmi < 30:
            return 2
        if 16.0 <= bmi < 18.5 or 30 <= bmi < 35:
            return 3
        else:
            return 4
    else:
        return 4


T = int(input())

for tc in range(T):
    height, weight = map(float, input().split())
    BMI = weight / ((height/100)**2)
    ans = check(height, BMI)
    print(ans)