mat = [
    [5, 2, 9],
    [1, 6, 3],
    [8, 7, 4]
]

target = int(input("Enter target: "))

found = False

for i in range(3):
    for j in range(3):
        if mat[i][j] == target:
            print(f"Found at ({i},{j})")
            found = True
            break
    if found:
        break

if not found:
    print("Not Found")