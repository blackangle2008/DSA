def subarraySum(nums, k):
    mp = {0: 1}  # important (for sum = k case)

    total_sum = 0
    count = 0

    for num in nums:
        total_sum += num

        if (total_sum - k) in mp:
            count += mp[total_sum - k]

        mp[total_sum] = mp.get(total_sum, 0) + 1

    return count


# Example usage
nums = [1, 1, 1]
k = 2

print("Number of subarrays:", subarraySum(nums, k))