nums = [0, 1, 0, 3, 12]

j = 0  # position for next non-zero

for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1

print(nums)