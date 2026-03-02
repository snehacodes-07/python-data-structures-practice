num_elements = int(input("Enter the number of elements: "))
elements_list = []

for _ in range(num_elements):
    element = input(f"Enter element: ")
    elements_list.append(element)

my_tuple = tuple(elements_list)

print(f"The input tuple is: {my_tuple}")
