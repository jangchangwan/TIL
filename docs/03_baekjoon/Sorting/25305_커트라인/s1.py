# 25305_커트라인
# 2022-06-25
# 정렬
N, K = map(int, input().split())
score = list(map(int, input().split()))

score.sort(reverse=True)
print(score[K-1])