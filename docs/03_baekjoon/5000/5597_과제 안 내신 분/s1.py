# 5597_과제 안 내신 분..?_문제풀이
# 2022-06-05


# 1~30번 학생 만들기
students = [i for i in range(1,31)]

# 제출 한 사람 제거
for _ in range(28):
    student = int(input())
    students.remove(student)

# 제출 안한 사람 출력
for student in students:
    print(student)