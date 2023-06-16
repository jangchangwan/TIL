

def postfix(post):
    temp = list(post)
    result = ""
    stack = []
    for i in temp:
        if i.isalpha():  
            result += i       

        elif i == '(':         
            stack.append(i)

        elif i == '*' or i == '/':      
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop() 
            stack.append(i)        

        elif i == '+' or i == '-':     
            while stack and stack[-1] != '(':
                result += stack.pop()  
            stack.append(i)        

        elif i == ')':       
            while stack and stack[-1] != '(':   
                result += stack.pop()    
            stack.pop()     

    while stack:    
        result += stack.pop()      

    return result

word = input()
answer = postfix(word)
print(answer)      
