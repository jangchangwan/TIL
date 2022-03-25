# 5648_원자-소멸-시뮬레이션-문제풀이
# 2022-03-25
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    # 각 원자들의 인덱스 만들어주기
    for i in range(N):
        atoms[i].insert(0, i)
    # 최대로 오래걸릴경우 3998 걸리므로
    time_arr = [[] for _ in range(4000)]
    # 충돌하는 시간,방향 넣기
    crash_atom = [[] for _ in range(N)]
    # 상하좌우를 인덱스를 따로 담기
    Up, Down, Left, Right = [], [], [], []
    for atom in atoms:
        if atom[3] == 0:
            Up.append(atom[0])
        elif atom[3] == 1:
            Down.append(atom[0])
        elif atom[3] == 2:
            Left.append(atom[0])
        else:
            Right.append(atom[0])
    # 충돌 가능성이 있는 것을 리스트에 담기
    # 상하 충돌
    for U in Up:
        for D in Down:
            if atoms[U][1] == atoms[D][1] and atoms[U][2] < atoms[D][2]:
                T = atoms[D][2] - atoms[U][2]
                time_arr[T].append(U)
                time_arr[T].append(D)
                crash_atom[U].append([T, D])
                crash_atom[D].append([T, U])
    # 좌우 충돌
    for L in Left:
        for R in Right:
            if atoms[L][2] == atoms[R][2] and atoms[R][1] < atoms[L][1]:
                T = atoms[L][1] - atoms[R][1]
                time_arr[T].append(L)
                time_arr[T].append(R)
                crash_atom[L].append([T, R])
                crash_atom[R].append([T, L])
    # 상좌 충돌
    for U in Up:
        for L in Left:
            if atoms[L][2] > atoms[U][2] and atoms[L][1] - atoms[U][1] == atoms[L][2] - atoms[U][2]:
                T = 2 * (atoms[L][1] - atoms[U][1])
                time_arr[T].append(L)
                time_arr[T].append(U)
                crash_atom[U].append([T, L])
                crash_atom[L].append([T, U])

    # 상우 충돌
    for U in Up:
        for R in Right:
            if atoms[R][2] > atoms[U][2] and atoms[U][1] - atoms[R][1] == atoms[R][2] - atoms[U][2]:
                T = 2 * (atoms[R][2] - atoms[U][2])
                time_arr[T].append(U)
                time_arr[T].append(R)
                crash_atom[U].append([T, R])
                crash_atom[R].append([T, U])

    # 하좌 충돌
    for D in Down:
        for L in Left:
            if atoms[D][2] > atoms[L][2] and (atoms[L][1] - atoms[D][1]) == (atoms[D][2] - atoms[L][2]):
                T = 2 * (atoms[L][1] - atoms[D][1])
                time_arr[T].append(D)
                time_arr[T].append(L)
                crash_atom[L].append([T, D])
                crash_atom[D].append([T, L])
    # 하우 충돌
    for D in Down:
        for R in Right:
            if atoms[D][2] > atoms[R][2] and atoms[D][1]-atoms[R][1] == atoms[D][2]-atoms[R][2]:
                T = 2 * (atoms[D][1]-atoms[R][1])
                time_arr[T].append(D)
                time_arr[T].append(R)
                crash_atom[D].append([T, R])
                crash_atom[R].append([T, D])

    ans = 0
    for i in range(4000):
        # 안에 충돌가능성이 있는거만 동작
        if time_arr[i]:
            # 중복 제거
            for atom in list(set(time_arr[i])):
                ans += atoms[atom][4]
                for j in range(i + 1, 4000):
                    # 만일 이후의 폭발에 원자가 포함되어 있다면
                    if atom in time_arr[j]:  
                        temp = []
                        for k in range(len(time_arr[j])):  
                            for w in range(len(crash_atom[atom])):
                                # 폭발한 바로 그 순간에 만나는 원자들이 리스트 안에 있을 경우
                                if crash_atom[atom][w][0] == j and (time_arr[j][k] in crash_atom[atom][w][1:]):
                                    temp.append(time_arr[j][k])
                        # 만일 충돌예정이었던 원소가 하나 뿐이라면, 해당 원소와의 충돌이 무산된다.
                        if len(temp) == 1:
                            time_arr[j].remove(temp[0])
                        while atom in time_arr[j]:
                            time_arr[j].remove(atom)
            # 끝난 후 초기화
            time_arr[i] = []
    print('#{} {}'.format(tc, ans))