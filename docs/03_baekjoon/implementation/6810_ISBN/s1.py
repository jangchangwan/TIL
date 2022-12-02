# 6810_ISBN

nums = "9780921418"
result = 0
for i in range(3):
    nums += str(input())

for i in range(13):
    if i % 2:
        result += int(nums[i]) * 3
    else:
        result += int(nums[i])

print("The 1-3-sum is", result)
