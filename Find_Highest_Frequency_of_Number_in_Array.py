# Find highest frequency element using hashing

n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter elements: ").split()))

# Hash map (dictionary) to store frequency
hash_map = {}

# Counting frequency
for num in arr:
    if num in hash_map:
        hash_map[num] += 1
    else:
        hash_map[num] = 1

# Finding element with highest frequency
max_freq = 0
max_element = None

for key in hash_map:
    if hash_map[key] > max_freq:
        max_freq = hash_map[key]
        max_element = key

print("Element with highest frequency:", max_element)
print("Frequency:", max_freq)