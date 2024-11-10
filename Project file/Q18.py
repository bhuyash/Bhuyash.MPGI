numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
target = int(input("Enter the number to search for: "))

found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        print(f"Number {target} found at index {i}")
        break

if not found:
    print(f"Number {target} not found in the list")
