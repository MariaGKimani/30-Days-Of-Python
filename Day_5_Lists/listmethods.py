# Declare an empty list
empty_list = []
empty_list1 =list()

#Declare a list with more than 5 items
list1 = ["cats","dogs","books","bottle","tissue"]
print(list1)
# Find the length of your list
print(len(list1))
# Get the first item, the middle item and the last item of the list
print(list1[0])
print(list1[-1])
print(len(list1)%2)

# Declare a list called mixed_data_types, 
# put your(name, age, height, marital status, address)
mixed_data_types =["Maria",22,177.0,"Single","Thika"]

# Declare a list variable named it_companies and
#  assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies =["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(list1[0])
print(list1[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'Kenya'
print(it_companies)

# Add an IT company to it_companies
it_companies[0] = 'Trigerrise'
print(it_companies)

#Insert an IT company in
# the middle of the companies list


# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]=it_companies[1].upper()
print(it_companies)
it_companies[2] =it_companies[2].upper()
print(it_companies)

# Join the it_companies with a string '#; 
x = "#".join(it_companies)
print(x)

# Check if a certain company exists in the it_companies list.
print('microsoft' in it_companies)
print('Microsoft' in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
# it_companies.reverse()
it_companies.sort(reverse=True)
print(it_companies)
# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
middle = len(it_companies)//2
print(middle)

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list



# Remove the last IT company from the list
it_companies.pop(-1)

# Remove all IT companies from the list
print(it_companies)

print(it_companies.pop(-1))

# Destroy the IT companies list
# del it_companies
# print(it_companies)


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
x= front_end + back_end
print(x)
front_end.extend(back_end)
print(front_end)
front_end.extend(['xxx','yyyyyy'])
print(front_end)

# After joining the lists in question above.
#  Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.
full_stack = x.copy()
print(full_stack)
full_stack.insert(0,'Python')
full_stack.insert(0,'Javascript')
print(full_stack)



