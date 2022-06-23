# 1439_뒤집기
# 2022-06-11


S = input()

ans = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        ans += 1

print((ans+1)//2)