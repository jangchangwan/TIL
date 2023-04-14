# 조건

# 한 문제를 여러번 제출 가능 최고점수로 기록
# 제출을 안한 경우 0점

# 최종 점수가 같을 경우 횟수가 적은팀이 우선순위
# 최종 점수와 횟수가 같을 경우 마지막 제출시간이 빠른팀이 우선순위


# 입력 아래순으로 입력
# T : 테스터 데이터 갯수
# team, problems, my_team_id, logs : 팀 수, 문제 수, 내팀 ID, 제출 횟수
# team_id, problem_no, score : 제출팀 id, 문제 번호, 점수


# 출력
# 내 팀 순위

# code
T = int(input())


for tc in range(T):
  team, problems, my_team_id, logs = map(int, input().split())
  board = [[0] * problems for _ in range(team)] # 현황판
  count = [0] * team # 제출 횟수
  time = [0] * team # 제출 시간
  for log in range(logs):
    team_id, problem_no, score = map(int, input().split())
    
    # 최고 점수로 갱신
    board[team_id - 1][problem_no - 1] = max(board[team_id - 1][problem_no - 1], score)
    # 제출 횟수 갱신
    count[team_id - 1] += 1
    # 제출 시간 갱신
    time[team_id - 1] = log

    
  new_board=[]
  for idx in range(len(board)):
      new_board.append([sum(board[idx]),count[idx],time[idx],idx])
      
  # 정렬
  new_board.sort(key=lambda x:(-x[0],x[1],x[2]))
  for idx in range(len(new_board)):
      if new_board[idx][3] == my_team_id-1:
          print(idx+1)
          break