numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Maximum value:", max_value)
print("Minimum value:", min_value)
