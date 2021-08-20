# When creating lists, lists must always be in square brackets
# print(type(my_list2)) tells you what type of list my_list2 creates
my_list = [1, 2, 3, 4, 5, 6]

my_list2 = list(range(1, 102, 10))
print(my_list)

# It creates a list(my_list 2) of numbers, beginning from one that increases by to. The list is up to 102
print(my_list2)

# Operations on lists

# How to get an element from a list
my_list1 = [1, 2, 3, 4, 5, 6]
# This command is telling the computer to take the second element  out of my_list1
# The list always begins zero, the zeroth element or the first element is 1
print(my_list1[2])
# This prints out the last element in the list
print(my_list1[-1])
# Let's create a slice from the second element to the 4th element
print(my_list1[1:4])

# Length of a list
print(len(my_list1))
# Maximum and Minimum elements of a list(highest number and lowest number)
print(max(my_list1))
print(min(my_list1))

# Add an element onto our list (The command adds a new element to the list
my_list1.append(120)
print(my_list1)

# How to reverse a list
my_list1.reverse()
print(my_list1)

# Create another list and add two lists together
my_list3 = [5, 4, 3, 2, 1]
print(my_list1 + my_list3)
