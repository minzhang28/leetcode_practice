# [1,3,5,6], 5, 2
# [1,3,5,6], 2, 1
nums = [1,3,5,6]
target = 4

return_val = 0
if target in nums:
    print(nums.index(target))
else:
    if target <= nums[0]:
        print(0)
    elif target >= nums[len(nums) - 1]:
        print(len(nums))
    else:
        for i in nums:
            if target <= i:
                print(nums.index(i))
                break
