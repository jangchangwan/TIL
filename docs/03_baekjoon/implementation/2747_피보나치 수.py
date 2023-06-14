

answer = [0, 1, 1]
for i in range(3, 46):
    answer.append(answer[i-2] + answer[i-1])
    
    

print(answer)
