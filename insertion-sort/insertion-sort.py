numbers = [100, 20, 10, 16, 6, 89]

for i in range(1, len(numbers)):
    j = i - 1
    curr = numbers[i]
    while j >= 0 and curr < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j+1] = curr

print("Mang sau khi sap xep - insertion sort: \n",numbers)
