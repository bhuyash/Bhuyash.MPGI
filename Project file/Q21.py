my_dict = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "date",
    5: "elderberry"
}

third_element = my_dict.get(3)
print("Third element:", third_element)

my_dict[4] = "dragonfruit"
print("Updated dictionary:", my_dict)

my_dict[6] = "fig"
print("Dictionary after adding new item:", my_dict)
