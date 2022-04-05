# 4831_전기버스
# 2022-02-10

# input.txt를 통해 입력값을 가져온다.
import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    # input.txt에서 한 번에 이동할 수 있는 정류장 수 K, 총 정류장 수 N, 설치된 정류장의 수 M을 받아온다.
    K, N, M = tuple(map(int, input().split()))
    # input.txt에서 M개의 정류장이 설치된 정류장 번호를 리스트로 받아온다.
    charger = list(map(int, input().split()))
    # 현재 전기 버스에 충전된 량을 표시하는 변수 charge를 설정한다. 출발지에는 충전기가 설치되어 있어 초기값이 K이다.
    charge = K
    # 지나친 정류장의 갯수를 셀 수 있는 변수 cnt를 설정 및 초기화한다.
    cnt = 0
    # 정류장을 지나치며 충전한 횟수를 세기 위한 변수 recharge를 설정 및 초기화한다.
    recharge = 0
    # 결과값을 받아오기 위한 변수 result를 설정 및 초기화한다.
    result = 0
    # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우를 위한 변수 fail을 설정 및 초기화한다.
    fail = 0

    # 총 N개의 정류장을 지나치는 동안 for문을 시행한다.
    for i in range(1, N+1):
        # 정류장을 하나 움직이는 순간 충전된 전기가 쓰이기에 현재 충전량을 표시하는 charge-1을 한다.
        charge -= 1

        # 마지막 충전소인 경우, 종점과 현재 정류장 간의 거리를 파악하여 충전을 할지, 하지 않을지를 결정한다.
        if cnt == M-1:
            if charger[cnt] == i:
                # 종점까지의 거리가 한 번에 이동할 수 있는 충전량 K보다 많으면 종점까지 도착할 수 없는 걸로 파악하고, fail+1을 한다.
                if N - charger[cnt] > K:
                    fail += 1
                # 종점까지의 거리가 현재 충전량보다는 완충량 K보다 작으면 충전이 필요하다고 파악하여 충전 횟수 recharge +1을 해준다.
                elif charge < N - charger[cnt] <= K:
                    recharge += 1
                    # 현재 충전량을 충전을 한 후이기에 완충량 K로 설정한다.
                    charge = K
                # 종점까지의 거리가 현재 충전량보다 적으면 충전할 필요가 없기 때문에 pass한다.
                elif charge >= N - charger[cnt]:
                    pass

        # 마지막 충전소가 아닌 경우, 다음 충전소가 있는 정류장과의 거리를 파악하여 충전을 할지, 하지 않을지를 결정한다.
        elif cnt < M-1:
            if charger[cnt] == i:
                # 다음 충전소까지의 거리가 한 번에 이동할 수 있는 충전량 K보다 많으면 종점까지 도착할 수 없는 걸로 파악하고, fail+1을 한다.
                if charger[cnt+1] - charger[cnt] > K:
                    cnt += 1
                    fail = 0
                # 다음 충전소까지의 거리가 현재 충전량보다는 완충량 K보다 작으면 충전이 필요하다고 파악하여 충전 횟수 recharge +1을 해준다.
                elif charge < charger[cnt+1] - charger[cnt] <= K:
                    recharge += 1
                    # 현재 충전량을 충전을 한 후이기에 완충량 K로 설정한다. 정류장을 하나 지났기 때문에 cnt+1을 한다.
                    charge = K
                    cnt += 1
                # 다음 충전소까지의 거리가 현재 충전량보다 적으면 충전할 필요가 없기 때문에 pass한다.
                elif charge >= charger[cnt+1] - charger[cnt]:
                    # 충전소를 한 번 거쳤기에 정류장을 지나친 횟수를 의미하는 cnt+1을 해준다.
                    cnt += 1
                    pass

    # 만약 fail이 한 번이라도 있으면 종점까지 도착할 수 없기에 result에 0을 저장한다.
    if fail > 0:
        result = 0
    # fail이 없다면 충전을 하면서 종점에 도착할 수 있는 것으로 보고 result에 recharge 값을 저장한다.
    else:
        result = recharge

    print('#{} {}'.format(tc, result))