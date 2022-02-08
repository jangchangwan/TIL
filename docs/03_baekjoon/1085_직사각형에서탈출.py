x,y,w,h = map(int,input().split())

result_list = [ x, y, w-x, h-y]

result = 1000
for num in result_list:
    if num <result :
        result = num
print(result)