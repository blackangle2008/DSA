nums = [1, 1, 2, 2, 3, 4, 4]

i = 0  # slow pointer

for j in range(1, len(nums)):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]

print("Unique elements:", nums[:i+1])
print("Length:", i + 1)