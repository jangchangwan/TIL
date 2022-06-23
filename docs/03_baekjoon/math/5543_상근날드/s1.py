
hamburger = [int(input()) for _ in range(3)]
drink = [int(input()) for _ in range(2)]

hamburger.sort()
drink.sort()

print(hamburger[0]+drink[0]-50)