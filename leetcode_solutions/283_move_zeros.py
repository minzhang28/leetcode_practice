nums = [0,1,0,3,12]

arr_aize = len(nums)
origin_size = len(nums)
i=0
while i < arr_aize:
    if nums[i] == 0:
        nums.remove(nums[i])
        arr_aize -= 1
        print("i is {}, nums is {}".format(i, nums))
        continue
    i += 1
new_size = len(nums)
counter = origin_size - new_size
print("counter sizer is {}".format(counter))
for x in range(counter):
    nums.append(0)

print(nums)
