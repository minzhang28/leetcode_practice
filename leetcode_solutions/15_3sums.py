nums = [-1, 0, 1, 2, -1, -4]
result = []
d = {}
nums.sort()
print("intput is {}".format(nums))
if len(nums) < 3:
    print(result)
else:
    for i in range(len(nums)):
        dic = {}
        for j in range(i+1, len(nums)):
            target = 0 - nums[i] - nums[j]
            if target in dic:
                if (nums[j],nums[i],target) not in d :
                    result.append([nums[j],nums[i],target])
                    print("i is {}, j is {}, value i is {}, value j is {}, target is {}, value to add is {}".format(i, j, nums[i], nums[j], target, result_to_check))
                    d[(nums[j],nums[i],target)]=1
            dic[nums[j]] = nums[j]
print(result)
return result
