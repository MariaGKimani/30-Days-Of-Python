# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

def score (grade):
    if grade >= 80 and grade <= 100:
        print("A")
    elif grade >= 70 and grade <= 89:
        print("B")
    elif grade >= 60 and grade <= 69:
        print("C")
    elif grade >= 50 and grade <= 59:
        print("D")
    elif grade >= 0 and grade <= 49:
        print("F")
grade1 = score(85)

# Check if the season is Autumn, Winter, Spring or Summer.
#  If the user input is: September, October or November, 
# the season is Autumn. December, January or February, 
# the season is Winter. March, April or May, 
# # the season is Spring June, July or August, the season is Summer

# x = "September","October","November"
# y = "December","January","February"
# z = "March","April","May"
# w = "June","July","August"
# person = input("Enter month: ")
# if person in x :
#     print("Autumn")
# elif person in y:
#     print("Winter")
# elif person in z:
#     print("spring")
# elif person in w:
#     print("summer")


# If a fruit doesn't exist in the list
# add the fruit to the list and
# print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']

def new_fruits (fruit):
     if fruit   in fruits:
         print('That fruit already exist in the list')
        
     else:
         fruits.append(fruit)
         print(fruits)

new_fruits('kiwi')
new_fruits('banana')

         










# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("Name a fruit: ")
# if fruit  in fruits:
#     print("that fruit already exist")
# else:
#     fruits.append(fruit)
#     print(fruits)
