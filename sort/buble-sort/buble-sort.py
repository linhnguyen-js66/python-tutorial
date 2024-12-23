numbers = [20, 10, 16, 6, 89]
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[i]:
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp

print("Mang sau khi sap xep - buble sort: \n",numbers)
