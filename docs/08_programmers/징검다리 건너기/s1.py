# 간단한 for문으로
# 생각해보니 배열의크기가 2*10^5이고 k가 10^5이면
# n^2이라서 10^10 시간초과가 당연했다
def solution(stones, k):
    answer = 200001
    for i in range(len(stones)-k+1):
        answer = min(answer, max(stones[i:i+k]))
    return answer