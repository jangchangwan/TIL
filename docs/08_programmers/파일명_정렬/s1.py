# 파일명_정렬_문제풀이
# 2022-04-09

# re class 사용
# re.split : 맞는 패턴을 기점으로 리스트를 쪼개준다.
import re


def solution(files):

    answer = []
    ans = []
    for file in files:
        temp = re.split("([0-9]+)", file)
        ans.append(temp)
    # 처음은 소문자 기준, 두번쨰는 숫자기준으로 정렬
    files = sorted(ans, key=lambda x: (x[0].lower(), int(x[1])))
    # join함수로 합치기
    for file in files:
        temp = ''.join(file)
        answer.append(temp)
    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))