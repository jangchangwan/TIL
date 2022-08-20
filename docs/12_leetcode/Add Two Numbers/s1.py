# Add Two Number
# 2022-08-20
# Runtime: 127 ms
# Memory Usage: 13.8 MB

# 두리스트는 역순으로 받아진다
# 두 숫자를 더하는 클래스를 만들어라

# Input 값만 보고 리스트 인줄 알았는데 낚였다
# ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
# ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, list1, list2):
        # 값
        num1 = 0
        num2 = 0

        # 첫번째 숫자
        position = 1
        while list1.next != None:
            num1 += list1.val * position
            position *= 10
            list1 = list1.next
        num1 += list1.val * position

        # 두번째 숫자
        position = 1
        while list2.next != None:
            num2 += list2.val * position
            position *= 10
            list2 = list2.next
        num2 += list2.val * position

        # 총합
        totalnum = num1 + num2

        # 총합 Object 만들기
        list3 = list(map(int, str(totalnum)))
        nodes = []
        for i in range(len(list3)):
            # 맨 안에 값은 Next가 없으므로 None을 넣는다
            if i == 0:
                node = ListNode(list3[i], None)
                nodes.append(node)
            # 아닌경우
            else:
                node = ListNode(list3[i], nodes[i - 1])
                nodes.append(node)

        return nodes[-1]
