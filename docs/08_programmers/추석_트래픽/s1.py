def solution(lines):
    answer = 0
    # 시간 만들기
    times = []
    # 응답 완료시간은 길이가 고정이므로
    # 슬라이싱으로 해결
    for line in lines:
        # 시, 분, 초, 마이크로초
        hour = int(line[11:13])
        minute = int(line[14:16])
        sec = int(line[17:19])
        msec = float(line[20:23]) * 0.001
        # 응답시간
        response = float(line[24:-1])

        # 처리시간이 시작, 끝시간이 포함되므로
        end = hour * 3600 + minute * 60 + sec + msec
        if end - response + 0.001 < 0:
            start = 0
        else:
            start = end - response + 0.001
        times.append([start, end])

        # 정렬되어 있는 상태이므로 모든 시간에서 볼필요없이 시작과 끝만 보면 된다.
        for i in range(len(times)):
            ans = 1
            temp = times[i][1] + 1
            j = i + 1
            while j < len(times):
                if temp > times[j][0]:
                    ans += 1
                j += 1
            answer = max(answer, ans)
    return answer