my_list = []

num_elements = int(input("How many elements would you like to append to the list? "))

for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

print("\nUpdated List:")
print(my_list)
