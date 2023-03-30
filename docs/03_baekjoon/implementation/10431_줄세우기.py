# 항상 20명 같은 키는 없음
# 


T = int(input())

for tc in range(T):
    # 입력
    data = list(map(int, input().split()))
    
    # 변수 초기화
    key = data[0]
    value = data[1:]
    result = 0
    
    sort_value = []
    # 실행
    for v in value:
        sort_value.append(v)
        temp_value = sorted(sort_value)
        
        prev = sort_value.index(v)
        after = temp_value.index(v)
        
        result += prev - after
        sort_value = temp_value
    
    # 출력
    print(f'{key} {result}')
    