# 외벽 점검_문제풀이
# 2022-05-01

from itertools import permutations


def solution(n, weak, dist):
    len_weak = len(weak)
    flag = False  # 취약지점 전부 점검 가능한지 판단
    min_answer = len(dist)  # 최소 인원을 총 친구의 수로 초기화

    # 한 바퀴를 완전히 도는 경우도 있으므로 한 바퀴 돌았을 때 취약지점의 위치를 가정함
    for i in range(len_weak):
        weak.append(weak[i] + n) # 한 바퀴 돈 이후의 취약지점의 위치 추가

    for order in list(permutations(dist, len(dist))):  # dist 원소의 순서에 따른 모든 경우의 수로 반복하여 최솟값 파악
        for start in range(0, len_weak):  # 시작위치
            index = 0
            position = weak[start] + order[index]  # 한명이 투입된 후의 현재위치
            index += 1
            answer = 1  # 투입된 인원 수
            wall = 0  # 점검한 외벽 수

            # start부터 점검
            i = start
            while True:
                if position >= weak[i]:  # 현재위치가 해당 취약지점 보다 앞서 있다면 점검 개수 1증가
                    wall += 1
                    i += 1
                    # 점검을 다한 경우
                    if wall == len_weak:
                        flag = True
                        min_answer = min(min_answer, answer)
                        break
                else:
                    if index >= len(order):  # 넘어갈경우
                        break
                    position = weak[i] + order[index]
                    index += 1
                    answer += 1
    if flag:
        return min_answer
    else:
        return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))

# 출력 에시
# 2
# 1

'''
테스트 1 〉	통과 (0.15ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (926.46ms, 14.8MB)
테스트 4 〉	통과 (912.83ms, 14.9MB)
테스트 5 〉	통과 (1.87ms, 10.3MB)
테스트 6 〉	통과 (204.37ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.35ms, 10.3MB)
테스트 9 〉	통과 (0.37ms, 10.3MB)
테스트 10 〉	통과 (1597.85ms, 14.9MB)
테스트 11 〉	통과 (1845.21ms, 14.9MB)
테스트 12 〉	통과 (1584.85ms, 14.9MB)
테스트 13 〉	통과 (1436.96ms, 14.8MB)
테스트 14 〉	통과 (1501.79ms, 14.9MB)
테스트 15 〉	통과 (1602.71ms, 15MB)
테스트 16 〉	통과 (1304.70ms, 14.9MB)
테스트 17 〉	통과 (1418.43ms, 14.8MB)
테스트 18 〉	통과 (1383.88ms, 14.8MB)
테스트 19 〉	통과 (1156.47ms, 14.9MB)
테스트 20 〉	통과 (1262.80ms, 14.9MB)
테스트 21 〉	통과 (1170.04ms, 14.9MB)
테스트 22 〉	통과 (0.32ms, 10.4MB)
테스트 23 〉	통과 (0.30ms, 10.3MB)
테스트 24 〉	통과 (0.30ms, 10.3MB)
테스트 25 〉	통과 (376.07ms, 15MB)
'''