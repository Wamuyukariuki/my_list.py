# creating an empty list
my_list = []
print(my_list)

# to append an items to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)


# to insert a value 15 to my_list
my_list.insert(1, 15)
print(my_list)

# to extend my_list with another
list = [50, 60, 70]
my_list.extend(list)
print(my_list)

# to remove the last element of my_list
my_list.remove(70)
print(my_list)

# sorting my_list in ascending order
my_list_ascending_order = my_list.sort()
print(my_list)

# to find the index of the value of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
