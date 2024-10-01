lst1=['Mathematics', 'chemistry', 1997, 2000,1, 2, 3, 2, 1]

#len():To find length of a list
print("Length of the list is:",len(lst1))

#count():To find frequency of given element in a list
print("Frequency of 1 in list is",lst1.count(1))

#append():To add an elemnt to the end of the list
print(lst1.append("hello"))

# Insert an item at a specific position
lst1.insert(2, 25)
print("After inserting 25 at index 2:", lst1)

# Remove an item from the list
lst1.remove(2000)
print("After removing 40:", lst1)

# Pop an item from the list (default is the last item)
popped_number = lst1.pop()
print("After popping an item:", lst1)
print("Popped item:", popped_number)

# Pop an item from a specific index
popped_number_at_index = lst1.pop(1)
print("After popping item at index 1:", lst1)
print("Popped item at index 1:", popped_number_at_index)

# Sort the list
lst1=[2,5,9,1,0,34,21,67,9,21,30]
lst1.sort()
print("Sorted list:", lst1)

# Reverse the list
lst1.reverse()
print("Reversed list:", lst1)

# Create a copy of the list
lst1_copy = lst1.copy()
print("Copy of the list:", lst1_copy)

# Clear the list
lst1.clear()
print("After clearing the list:", lst1)

# Extend the list with another list
more_lst1 = [70, 80, 90]
lst1.extend(more_lst1)
print("After extending with more lst1:", lst1)

#Nesting in list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list is:",nested_list)

print("Element at index 0:",nested_list[0])

# Accessing an element from the first inner list
print("Accesing inner list element:",nested_list[0][1]) 
