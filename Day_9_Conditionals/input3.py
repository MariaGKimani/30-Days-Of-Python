person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#  Check if the person dictionary has skills key,
#  if so print out the middle skill in the skills list.
if "skills" in person:
    print('Skills exists')

print(person['skills'])
#convert it to tuple
# skill= list(person.items())
# middle_index = len(skill)//2
# middle_key,middle_value = person[middle_index]
# print(middle_key,middle_value)




# Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill 
# and print out the result.
if "skills" in person:
    print('Skills exists')
value  = person['skills']
# print(person['skills'])
print(value)

if "Python" in "skills":
    print("exists")
# getting the index of python


#  If a person skills has only JavaScript and React,
#  print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB,
#  print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB,
#  Print('He is a fullstack developer'),
#  else print('unknown title') - 
# for more accurate results more conditions can be nested!











#  If the person is married and if he lives in Finland, 
# print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.