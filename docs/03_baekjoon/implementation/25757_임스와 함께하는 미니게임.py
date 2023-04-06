people, type = map(str, input().split())


role = {
    "Y" : 1,
    "F" : 2,
    "O" : 3
}

members = set()

for i in range(int(people)):
    member = input()
    members.add(member)

print(len(members) // role[type])