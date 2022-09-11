class Solution:
    def calculate(self, s):

        stack = []
        operator, number = '+', 0

        for chr in s:
            # 숫자인지 체크
            if chr.isdigit():
                number = number * 10 + int(chr)

            # 연산자인 경우
            elif chr in "+-*/":

                if operator == "+":
                    stack.append(number)
                elif operator == "-":
                    stack.append(-number)
                elif operator == "*":
                    stack.append(stack.pop() * number)
                else:
                    stack.append(int(stack.pop() / number))

                operator, number = chr, 0

        # 마지막 숫자 넣어주기 위해서
        if operator == "+":
            stack.append(number)
        elif operator == "-":
            stack.append(-number)
        elif operator == "*":
            stack.append(stack.pop() * number)
        else:
            stack.append(int(stack.pop() / number))

        answer = sum(stack)
        return answer

