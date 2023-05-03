import math
# # Declare a function named evens_and_odds . 
# # It takes a positive integer as parameter
# # and it counts number of evens and odds in the number.
def evens_and_odds(postveInt):
    even =0
    odd =0
    number = str(postveInt)
    for digit in number:
        if int(digit) %2 ==0:
            even +=1
        else:
            odd +=1
    return even,odd
print(evens_and_odds(223344))

# # Call your function factorial, 
# # it takes a whole number as a parameter 
# # and it return a factorial of the number
# def factorial(wholeNum):
#     x=  math.factorial(wholeNum)
#     return x
# print(factorial(25))
# def num_greater_average(num):


# # Call your function is_empty,
# #  it takes a parameter 
# # and it checks if it is empty or not
def is_empty(empt):
    if empt:
        return True
    else:
        return False
print(is_empty("Maria"))
print(is_empty(""))


# Write a function called is_prime, which checks if a number is prime

# remove duplicates
def list_of_integers(nums):
    return list(set(nums))
list_of_integers([1,2,3,4,4,5,8,9,9])


def xx(num1,num2):
    x = math.factorial(num1,num2)
    return x
print(xx)

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).










    

