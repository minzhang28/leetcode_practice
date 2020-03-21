# [1,3,5,6], 5, 2
# [1,3,5,6], 2, 1
import time
height =[2,3,4,5,18,17,6]

start_time = time.time()
l = 0
r = len(height)-1
result = 0

while l <= r:
    min_height = min(height[l], height[r])
    temp = min_height * abs(l - r)
    # print("l is {}, r is {}, dis is {}, value l is {}, value r is {}, temp is {}, result is {}".format(l, r, abs(l-r), height[l], height[r], temp, result))
    result = max(result, temp)
    if height[l] < height[r]:
        l = l + 1
    else:
        r = r - 1
end_time = time.time()
print("execution_time is {}".format(end_time-start_time))
print("result is {}".format(result))
