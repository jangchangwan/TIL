from collections import defaultdict


#투 포인트
def solution(gems):
    length = len(gems)
    kind_gems = len(set(gems))
    gems_cnt = defaultdict(int)
    answer = [0, length]
    start, end = 0, -1

    while start < length and end < length:
        # 보석 종류가 다 있을 경우
        if len(gems_cnt) == kind_gems:
            # 최소값인지
            if answer[1] - answer[0] > end - start:
                answer = [start+1, end+1]
            # start를 증가해서 맨 앞 보석 제거하고 다시 확인
            gems_cnt[gems[start]] -= 1
            if gems_cnt[gems[start]] == 0:
                gems_cnt.pop(gems[start])
            start += 1
        # 보석 종류가 없을 경우
        else:
            end += 1
            if end < length:
                gems_cnt[gems[end]] += 1
    return answer