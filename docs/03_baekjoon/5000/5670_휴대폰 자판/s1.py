# 5670_휴대폰 자판_문제풀이
# 2022-05-09

import sys
sys.stdin = open('input.txt', 'r')

# 첫글자는 무조건 눌러야한다
# 입력
# 부모에 자식이 몇개있는지 넣을때마다 cnt를 올린다.
# 찾기
# 자식이 1개 일경우 계속탐색
# 자식이 2개이상일경우 cnt 를 1씩늘려준다
# cnt 출력
# 평균값 구하기


# 트라이 자료구조 정의
class Node(object):
    def __init__(self, head, word=None):
        self.head = head
        self.word = word
        self.children = {}
        self.child_nums = 0


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        # 현재 위치 => 루트 노드
        curr_node = self.head

        # 삽입하기 위한 절차
        for char in string:
            # 문자가 자식에 없으면
            if char not in curr_node.children:
                # 자식 집합에 노드 생성
                curr_node.children[char] = Node(char)
                curr_node.child_nums += 1
            curr_node = curr_node.children[char]
        # 데이터 삽입
        curr_node.word = string

    def search(self, string):
        curr_node = self.head
        cnt = 1
        # 탐색
        for idx, char in enumerate(string):
            if char in curr_node.children:
                # 자식이 하나 이상이면 버튼을 눌러야하므로 카운트
                if (curr_node.child_nums > 1 or curr_node.word) and idx:
                    cnt += 1
                curr_node = curr_node.children[char]
        # 탐색 종료 후 카운트 반환
        return cnt


while True:
    try:
        N = int(input())
        trie = Trie()
        # 입력
        words = [input() for _ in range(N)]
        for i in range(N):
            trie.insert(words[i])
        total = 0
        for i in range(N):
            total += trie.search(words[i])
        # 소숫점 둘째 자리까지 반올림
        print('{:.2f}'.format(round(total/N, 2)))
    except:
        break

# 출력예시
# 2.00
# 1.67
# 2.71