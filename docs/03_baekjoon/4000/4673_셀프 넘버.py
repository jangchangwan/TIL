number_list = list()
for num in range(1,10001):
    number_list.append(num)

constructor_list = list()
for num in number_list:
    
    for s in str(num):
        num += int(s)
    constructor_list.append(num)

for con in constructor_list:
    if con in number_list:
        number_list.remove(con)
    #print(number_list)
for num in number_list:
    print(num)

