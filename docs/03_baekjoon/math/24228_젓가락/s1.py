# 24228_젓가락
# 2022-06-30
# 수학

'''
최악의 경우
N종류의 젓가락을 모두 한개씩 뽑은 뒤 R를 완성할 때까지 한종류의 젓가락만 계속 뽑는 경우
'''
N, K = map(int, input().split())

answer = N + K * 2 - 1
print(answer)