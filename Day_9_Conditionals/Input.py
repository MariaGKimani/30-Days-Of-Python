# # Get user input using input(“Enter your age: ”). 
# # If user is 18 or older, give feedback: 
# # You are old enough to drive. If below 18 give feedback to wait for 
# # the missing amount of years
age =int(input("Enter your age: "))
if age >= 18:
    print ("You're old enough to drive")
else:
    missing_years = 18-age
    print("You need to wait", missing_years, "more year(s) before you can drive.")


# # Compare the values of my_age
# # and your_age using if … else. 
# # Who is older (me or you)? 
# # Use input(“Enter your age: ”) to get the age as input.
# #  You can use a nested condition to print 'year' for 1 year difference in age, 
# #  'years' for bigger differences, and a custom text if my_age = your_age. 

my_age =22
your_age = int(input("Enter your age: "));
difference = your_age -my_age
if difference == -1:
    print("year")
else:
    my_age = your_age
    print("good")


# # Get two numbers from the user using input prompt. 
# # If a is greater than b return a is greater than b, 
# # if a is less b return a is smaller than b, else a is equal to b.
# def numbers():
#     a = int(input("Enter a number:"))
#     b = int(input("Enter a number:"))
#     if a > b:
#         return "a is greater than b"
#     elif a < b:
#         return "a is smaller than b"
#     else:
#         return "a is equal to b"
    
# print(numbers())


a = int(input("Enter a String:"))

x = a[::-1]
print(x)

