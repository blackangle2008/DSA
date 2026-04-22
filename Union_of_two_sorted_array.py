arr1 = [1, 2, 4, 5]
arr2 = [2, 3, 5, 6]

n1 = len(arr1)
n2 = len(arr2)

i = j = 0

print("Union:", end=" ")

while i < n1 and j < n2:
    # Skip duplicates in arr1
    if i > 0 and arr1[i] == arr1[i - 1]:
        i += 1
        continue

    # Skip duplicates in arr2
    if j > 0 and arr2[j] == arr2[j - 1]:
        j += 1
        continue

    if arr1[i] < arr2[j]:
        print(arr1[i], end=" ")
        i += 1
    elif arr2[j] < arr1[i]:
        print(arr2[j], end=" ")
        j += 1
    else:
        print(arr1[i], end=" ")
        i += 1
        j += 1

# Remaining elements
while i < n1:
    if i == 0 or arr1[i] != arr1[i - 1]:
        print(arr1[i], end=" ")
    i += 1

while j < n2:
    if j == 0 or arr2[j] != arr2[j - 1]:
        print(arr2[j], end=" ")
    j += 1