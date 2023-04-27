"""
4
DOG
GOD
GOOD
DOLL
"""

# 입력
N = int(input())
words = [list(input()) for _ in range(N)]

# 변수 초기화
count = 0

for i in range(1, N):
    # 얕은 복사
    main_word = words[0][:]
    sub_word = words[i]
    
    no = 0
    for word in sub_word:
        if word in main_word:
            main_word.remove(word)
        else:
            no += 1

    if no <= 1 and len(main_word) <= 1:
        count += 1
        
print(count)

