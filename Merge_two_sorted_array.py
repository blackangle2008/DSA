arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

n1 = len(arr1)
n2 = len(arr2)

merged = []

i = j = 0

# Merge arrays
while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

# Remaining elements
while i < n1:
    merged.append(arr1[i])
    i += 1

while j < n2:
    merged.append(arr2[j])
    j += 1

# Print result
print("Merged Array:", merged)