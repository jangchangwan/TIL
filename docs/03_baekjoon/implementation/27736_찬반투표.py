# 문제
# 중앙대학교에서 재학생을 대상으로 하는 어떤 찬반투표가 치러졌다. 모든 재학생은 각자 찬성이나 반대, 혹은 기권 중 하나로 투표에 응답하였다.

# 해당 투표에서 찬성이 반대보다 많으면 투표가 통과된다. 반대가 찬성보다 많거나, 반대와 찬성의 수가 동일하다면 투표는 통과되지 않는다. 
# 단, 기권한 사람이 재학생의 절반 이상이라면 찬성과 반대의 수와 관계없이 항상 투표는 무효 처리된다.

# 재학생들의 투표 내역을 입력받아 찬반투표의 결과를 출력하는 프로그램을 구현하시오.

# 입력
# 첫 번째 줄에 중앙대학교 재학생의 수 
# $N$이 주어진다.

# 두 번째 줄에 
# $N$개의 투표 내역이 공백으로 구분되어 주어진다. 각각 찬성은 1, 반대는 -1, 기권은 0으로 주어진다.

# 출력
# 투표가 통과되었으면 APPROVED, 통과되지 않았으면 REJECTED, 무효 처리되었으면 INVALID를 출력한다.

# 제한

# 예제 입력 1 
# 5
# 1 -1 1 1 -1
# 예제 출력 1 
# APPROVED


N = int(input())
arr = list(map(int, input().split()))

agree = arr.count(1)
disagree = arr.count(-1)
null_count = arr.count(0)

if null_count >= N / 2:
    print("INVALID")
elif agree > disagree:
    print("APPROVED")
else:
    print("REJECTED")