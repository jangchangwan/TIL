# 2083_럭비클럽
# 2022-08-16
# 구현

while True:
    name, age, kg = input().split()

    if name == "#" and age == "0" and kg == "0":
        break

    if int(age) > 17 or int(kg) >= 80:
        print(name+" Senior")
    else:
        print(name+" Junior")