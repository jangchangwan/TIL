import itertools

def get_MBTI_distance(person1, person2):
    result = 0
    for i in range(4):
        if person1[i] != person2[i]:
            result += 1
            
    return result 

    

T = int(input())

for tc in range(T):
    N = int(input())
    characters = list(map(str, input().split()))
    
    if N > 32:
        print(0)
    else:    
        nPr = itertools.permutations(characters, 3)
        answer = 987654321   
        for value in nPr:
            
            temp = 0
            temp += get_MBTI_distance(value[0], value[1])
            temp += get_MBTI_distance(value[1], value[2])
            temp += get_MBTI_distance(value[0], value[2])
            
            answer = min(temp, answer)
        
        print(answer)