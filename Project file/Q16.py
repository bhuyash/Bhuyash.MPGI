list1 = input("Enter elements of the first list separated by space: ").split()
list2 = input("Enter elements of the second list separated by space: ").split()

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

sum_list = []
for i in range(min(len(list1), len(list2))):
    sum_list.append(list1[i] + list2[i])

print("Sum of the lists:", sum_list)
