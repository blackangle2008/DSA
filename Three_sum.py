arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)

arr.sort()

print("Triplets are:")

for i in range(n - 2):
    # Avoid duplicates
    if i > 0 and arr[i] == arr[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:
        s = arr[i] + arr[left] + arr[right]

        if s == 0:
            print(arr[i], arr[left], arr[right])

            # Skip duplicates
            while left < right and arr[left] == arr[left + 1]:
                left += 1
            while left < right and arr[right] == arr[right - 1]:
                right -= 1

            left += 1
            right -= 1

        elif s < 0:
            left += 1
        else:
            right -= 1