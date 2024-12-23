numbers = [20, 10, 16, 6, 89, 1, 5, 9, 100]

# Divide
def divide(numbers, start, end):
    if start == end:
        return [numbers[start]]
    else:
        middle = (start + end) // 2
        left_numbers = divide(numbers, start, middle) 
        right_numbers = divide(numbers, middle+1, end)
        return conquer(numbers, left_numbers, right_numbers)
    
# Sort
def conquer(numbers, left_numbers, right_numbers):
    new_nums = []
    i = 0
    j = 0
    while i < len(left_numbers) and j < len(right_numbers):
        if left_numbers[i] < right_numbers[j]:
            new_nums.append(left_numbers[i])
            i += 1
        else:
            new_nums.append(right_numbers[j])
            j += 1
    if i < len(left_numbers):
        new_nums += left_numbers[i:]
        
    if j < len(right_numbers):
        new_nums += right_numbers[j:]
    return new_nums

divide(numbers, 0, len(numbers)-1)