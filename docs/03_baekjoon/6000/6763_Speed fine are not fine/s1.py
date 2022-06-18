# 6763_Speed fine are not fine
# 2022-06-18

a = int(input())
b = int(input())

over = b - a
if a - b >= 0:
    print('Congratulations, you are within the speed limit!')
else:
    if 0 <= over < 21:
        print('You are speeding and your fine is $100.')
    elif 21 <= over < 31:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $500.')