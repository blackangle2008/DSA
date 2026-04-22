arr = [1, 2, 3]
n = len(arr)

# Step 1: Find pivot
i = n - 2
while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1

if i >= 0:
    # Step 2: Find next greater element
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    
    # Swap
    arr[i], arr[j] = arr[j], arr[i]

# Step 3: Reverse remaining
arr[i + 1:] = reversed(arr[i + 1:])

print("Next Permutation:", arr)