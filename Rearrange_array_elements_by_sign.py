def rearrangeArray(nums):
    n = len(nums)
    result = [0] * n

    pos = 0  # index for positive numbers
    neg = 1  # index for negative numbers

    for num in nums:
        if num > 0:
            result[pos] = num
            pos += 2
        else:
            result[neg] = num
            neg += 2

    return result


# Example usage
nums = [3, -1, -2, 4, -3, 5]

ans = rearrangeArray(nums)

print("Rearranged array:", *ans)