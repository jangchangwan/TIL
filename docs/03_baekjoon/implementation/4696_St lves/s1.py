# 4696_St. lve
# 2022-08-22



while True:
    N = float(input())

    if N:
        answer = 1 + N + N ** 2 + N ** 3 + N ** 4
        answer = round(answer, 2)
        print(f'{answer:.2f}')
    else:
        break
