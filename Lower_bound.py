def lower_bound(arr, key):
    low = 0
    high = len(arr) - 1
    ans = len(arr)  # default if not found

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= key:
            ans = mid
            high = mid - 1  # go left
        else:
            low = mid + 1  # go right

    return ans


# Example
arr = [1, 3, 3, 5, 7]
key = 3

index = lower_bound(arr, key)
print("Lower Bound Index:", index)