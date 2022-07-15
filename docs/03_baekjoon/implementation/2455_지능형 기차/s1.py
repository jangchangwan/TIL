# 2455_지능형 기차
# 2022-07-14



time = []
people = 0

for _ in range(4):
    remove_people, add_people = map(int, input().split())
    people += (add_people - remove_people)
    time.append(people)

answer = max(time)
print(answer)