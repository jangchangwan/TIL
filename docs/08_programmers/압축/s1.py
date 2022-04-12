# 압축_문제풀이
# 2022-04-09

# 우선 A~Z 까지 사전을 chr함수를 사용하여 만들었다.
# 사전에 있을경우 출력하고 다음글자를 추가해서 탐색을 반복
# 사전에 없을 경우 사전에 추가해준다
my_dictionary = {}
for i in range(65, 91):
    my_dictionary[chr(i)] = i - 64


def solution(msg):
    global my_dictionary
    answer = []
    # A - Z 까지 사전만들기

    num = 26
    front = 0
    rear = len(msg)
    while front < rear:
        k = 1 # 단어크기
        # 사전에 단어가 있을경우
        while msg[front:front+k] in my_dictionary and front+k <= len(msg):
            k += 1
        # 없을경우 사전에 등록
        if not msg[front:front+k] in my_dictionary:
            num += 1
            my_dictionary[msg[front:front+k]] = num

        answer.append(my_dictionary[msg[front:front+k-1]])
        front += k-1
    return answer


print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))