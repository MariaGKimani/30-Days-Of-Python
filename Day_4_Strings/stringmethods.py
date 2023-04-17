#Declare a variable named company and 
# assign it to an initial value "Coding For All".

company ="Coding For All"
print(company)

#Print the length of the company string
#  using len() method and print().
print(len(company))

#Change all the characters to uppercase
#  letters using upper() method.
print(company.upper())

#Change all the characters to lowercase 
# letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods 
# to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of 
# Coding For All string.
x =company[0:6]
print(x)

# Check if Coding For All string contains a word Coding 
# using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))

#Replace the word coding in
#  the string 'Coding For All' to Python.

print(company.replace("Coding","Python"))

#Change Python for Everyone to 
# Python for All using the replace method or other methods.
print(company.replace("All", "Everyone"))
print(company)

#Split the string 'Coding For All' 
# using space as the separator (split()) 
company.split(" ")
print(company)

#"Facebook, Google, Microsoft, Apple, IBM,
# Oracle, Amazon" split the string at the comma.
companies ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(companies.split(","))


#What is the character at index 0
# in the string Coding For All
print(company[0])

#What is the last index of 
# the string Coding For All.
print(len(company)-1)

#What character is at
#  index 10 in "Coding For All" string.
print(company[10])

#Create an acronym or an abbreviation
#  for the name 'Python For Everyone'.



#Use index to determine the position of the first
# occurrence of C in Coding For All.
print(company.index('C'))


#Use index to determine the position of the first
#  occurrence of F in Coding For All.
print(company.index('F'))
# Use rfind to determine the position of the last
#  occurrence of l in Coding For All People
co = "Coding For All People"
print(co.rfind("l"))

#Use index or find to find the position of the first
# occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent.find('because'))

print(sent.index('because'))


#Use rindex to find the position of the last 
# occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sent.rindex('because'))
print(sent.rfind('because'))

#Slice out the phrase 'because because because' 
# in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sent[31:48])


#Find the position of the first occurrence of the word 
# 'because' in the following sentence: '
# You cannot end a sentence with because because because is a conjunction
print(sent.find('because'))

#Does ''Coding For All' start
#  with a substring Coding?
print(company)
print(company.startswith('Coding'))
print(company.endswith('coding'))


#'   Coding For All      '  , 
# remove the left and right trailing spaces in the given string.
xx = '   Coding For All      ' 
print(xx.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
cc = '30DaysOfPython'
dd = 'thirty_days_of_python'
print(cc.isidentifier())
print(dd.isidentifier())

#The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string


#34 Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

#33
#Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

ss= "I am enjoying this challenge.\nI just wonder what is next."
print(ss)



# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
fs ='The area of a circle with {}  is + {}  squares'.format(radius,area )
print(fs)



#Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 26214

