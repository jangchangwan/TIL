# 가희와 카오스 파풀라투스_문제풀이
# 2022-06-08

# 패턴 제거
def remove_time(time):
    global score
    if 0 < time < 120:
        score[0] = 0
    elif 120 < time < 240:
        score[1] = 0
    elif 240 < time < 360:
        score[2] = 0
    elif 360 < time < 480:
        score[3] = 0
    elif 480 < time < 600:
        score[4] = 0
    elif 600 < time < 720:
        score[5] = 0


now_time = input().split(':')
score = list(map(int, input().split()))

M = int(input())
skills = [list(input().split()) for _ in range(M)]

# 현재시간을 분으로 나누기
now = int(now_time[0]) * 60 + int(now_time[1])

for skill in skills:
    if float(skill[0]) > 60 or sum(score) == 0:
        break
    else:
        if skill[1] == '^':
            remove_time(now)
        else:
            if skill[1][2:] == 'MIN':
                now += int(skill[1][:2])
            else:
                now += int(skill[1][:1])*60

        if now > 720:
            now -= 720

if sum(score) >= 100:
    print(100)
else:
    print(sum(score))