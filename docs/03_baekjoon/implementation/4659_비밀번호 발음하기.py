# 구현
vowels = ['a', 'e', 'i', 'o', 'u']


# 1. 모음 체크
def IsVowels(password):
    vowels_flag = False
    for vowel in vowels:
        if vowel in password:
           vowels_flag = True
    
    # 모음이 없을 경우 False 
    if vowels_flag == False:
        return False
    return True


# 2. 모음이 연속 3번 or 자음 연속 3번
def IsTriple(password):
    vowels_count = 0
    novowels_count = 0
    
    for word in password:
        if word in vowels:
            vowels_count += 1
            novowels_count = 0
        else:
            vowels_count = 0
            novowels_count += 1
        
        if vowels_count >= 3 or novowels_count >= 3:
            return False
    return True

# 3. 같은 단어 체크
def IsTwin(password):
    pass_keyword = ["e", "o"]
    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i] not in pass_keyword:
            return False
    return True


def Solution(password):
    if IsVowels(password) and IsTriple(password) and IsTwin(password):
        return True
    return False


while True:
    # 입력
    password = input()
    
    # 종료조건
    if password == "end":
        break
    
    # 실행
    if Solution(list(password)):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
    


