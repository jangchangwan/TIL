# 4999_아!_문제풀이
# 2022-06-05


# 입력
patient = input()
doctor = input()

# a 갯수 카운팅
patient_A = patient.count('a')
doctor_A = doctor.count('a')

# 출력
if patient_A < doctor_A:
    print('no')
else:
    print('go')