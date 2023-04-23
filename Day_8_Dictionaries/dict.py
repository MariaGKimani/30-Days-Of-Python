# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name':'Rottweilers',
    'color': 'Black',
    'breed': 'xxxx',
    'legs':  4,
    'age': 34,
}
# Create a student dictionary and add first_name, last_name,
# gender, age, marital status, skills, country, 
# city and address as keys for the dictionary
student ={
    'first_name': 'Mariagoretti',
    'last_Name' : 'Kimani',
    'gender'  : 'Female',
    'age'  : 22,
    'marital status': 'Single',
    'skills':['HTML','CSS','Javascript','Python','collaboration','Dart'],
    'country': 'Kenya',
    'city' : "Nairobi",
    'Address': {
   ' street' :'Riara lane',
   'zipcode' : '3400-0100'
    }
}
# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check 
# the data type, it should be a list
# x = student['skills'].values()
# print(x)

# Modify the skills values by adding one or two skills
student['skills'].append('Java')
student['skills'].append('Nodejs')
print(student)

# Get the dictionary keys as a list
xx = student.keys()
print(xx)
# Get the dictionary values as a list
yy = student.values()
print(yy)
# Change the dictionary to a list of
#  tuples using items() method

print(student.items())
print(type(student))


# Delete one of the items in the dictionary
del student['skills']
print(student)


# Delete one of the dictionaries
del dog
print(dog)


