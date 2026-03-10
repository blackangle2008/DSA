arr = [10,20,60,40,50]
n =len(arr)
max = arr[0]
for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
    
print(max)