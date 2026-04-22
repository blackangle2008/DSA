def search_rotated(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# Example
arr = [4, 5, 6, 7, 0, 1, 2]
target = int(input("Enter element to search: "))

result = search_rotated(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")