numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
item_to_remove = int(input("Enter the number to remove: "))

while item_to_remove in numbers:
    numbers.remove(item_to_remove)

print("Updated list:", numbers)
