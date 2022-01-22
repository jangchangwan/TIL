
def odd(n):
    if n % 2 : # 나머지가 1일경우 True => 홀수 찾기
        return True
    return False # 아닐경우 나머지가 0 이므로 => 짝수 찾기

def even(n):
    if n % 2 :
        return False # 홀수일 때 False 반환
    return True  # 짝수일 때 True 반환