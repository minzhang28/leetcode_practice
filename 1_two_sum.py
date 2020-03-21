nums = [3,3]
target = 6

result = []
for i in enumerate(nums):
    j = target - i
    if j in rest_nums:
        result.append(nums.index(i))
        result.append(nums.index(i) + rest_nums.index(j) + 1)
        print(result)
        break
