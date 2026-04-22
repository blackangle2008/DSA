def merge(arr, low, mid, high):
    count = 0

    # Count reverse pairs
    j = mid + 1
    for i in range(low, mid + 1):
        while j <= high and arr[i] > 2 * arr[j]:
            j += 1
        count += (j - (mid + 1))

    # Merge step
    temp = []
    i, j = low, mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    # Copy back
    arr[low:high+1] = temp

    return count


def merge_sort(arr, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2

        count += merge_sort(arr, low, mid)
        count += merge_sort(arr, mid + 1, high)
        count += merge(arr, low, mid, high)

    return count


# Example
arr = [1, 3, 2, 3, 1]
result = merge_sort(arr, 0, len(arr) - 1)

print("Reverse Pairs:", result)