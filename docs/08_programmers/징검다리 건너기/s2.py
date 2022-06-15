# 이분탐색으로 건널수 있는 사람의 수를 분할해서 탐색하자
# 효율성에서 4개정도 성공
# 방식은 맞는데 check 함수에서 while문안에 if문이 2개인게 문제인듯하다.


def checkstone(man, stones, power):  # 징검다리 건널 수 있는지 체크하는 함수
    # 현재 위치
    now = -1
    # 다음 건널 돌
    next = 0
    while next < len(stones):
        # 건너갈 수 있는 경우
        if stones[next] >= man:
            #
            now = next
            next += 1
        # 건너갈순있지만 뛰어넘아야되는 경우
        else:
            next += 1
        # 건널 수 없는 경우
        if next - now > power:
            return False
    return True


def solution(stones, k):
    left = 1
    # 최대 배열의 크기
    right = int(2e8)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if checkstone(mid, stones, k):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer