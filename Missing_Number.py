nums = [3, 0, 1]

missing = len(nums)

for i in range(len(nums)):
    missing ^= i ^ nums[i]

print(missing)