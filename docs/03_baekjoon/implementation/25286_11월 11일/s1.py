from datetime import datetime,timedelta
T = int(input())

for tc in range(T):
    year, m = map(int, input().split())

    time = datetime(year, m, m)
    answer = time + timedelta(days=-m)
    print(answer.year, answer.month, answer.day)