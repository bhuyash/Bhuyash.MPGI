dictionary = {}

n = int(input("How many key-value pairs would you like to enter? "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

print("The resulting dictionary is:", dictionary)
