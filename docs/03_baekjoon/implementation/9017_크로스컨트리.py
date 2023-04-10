# 6명이 한팀
# 상위 4명 점수 합산
# 가장 낮은 점수를 가진 팀이 승리
# 6명이 팀이 아닐경우 제외
# 동점일경우 다섯번째 주자 점수 체크

# 여섯명보다 많은팀은 없다
# 적어도 한팀은 6명
# 모든 선수가 끝까지 완주한다는 가정

T = int(input())

for tc in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    
    count = 1               # 점수
    team_score = [0] * N    # 팀 스코어
    team = []               # 6명인 팀
    team_member = [0] * N   # 팀 멤버 수
    five_score = [0] * N    # 다섯번째 사람 점수
    
    # 6명인 팀 찾기
    for i in range(1, N+1):
        if score.count(i) == 6:
            team.append(i)

    # 팀 스코어 얻기 + 5번째 팀원 점수 얻기
    for s in score:
        if s in team:
            team_member[s-1] += 1
            if team_member[s-1] < 5:
                team_score[s-1] += count
            if team_member[s-1] == 5:
                five_score[s-1] = count
            count += 1
        
    # 필터
    min_value = 987654321
    winner = N-1
    for t in team:
        if team_score[t-1] < min_value:
            min_value = team_score[t-1]
            winner = t
        
        elif team_score[t-1] == min_value and five_score[t-1] < five_score[winner-1]:
            winner = t
    

    print(winner)