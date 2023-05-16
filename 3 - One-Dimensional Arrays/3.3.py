arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_arr = []

for i in arr:
    if i % 2 != 0:
        new_arr.append(i)

print(new_arr)