#  Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1,num2):
    return num1+num2

print(add_two_numbers(24,10))


# Area of a circle is calculated as follows: area = π x r x r.
#  Write a function that calculates area_of_circle
def area_of_circle(radius):
    return 3.14 *radius*radius
print(area_of_circle(10))

# Write a function called add_all_nums which takes arbitrary 
#  of arguments and sums all the arguments. 
# Check if all the list items are number types.
#  If not do give a reasonable feedback.
# def add_all_nums(*addd):
#     total = 0
#     for i in addd:
        


# Temperature in °C can be converted to °F using this formula:
# °F = (°C x 9/5) + 32. Write a
# function which converts °C to °F, convert_celsius_to-fahrenheit

def convert_celsius_to_fahrenheit(celcius):
 return (celcius *9/5) +32

print(convert_celsius_to_fahrenheit(32))

# Write a function called check-season, 
# it takes a month parameter and returns 
# the season: Autumn, Winter, Spring or Summer.
def check_season(month):
   if month in['December','January','February']:
      return 'Winter'
   elif month in ['March','April','May']:
      return 'Spring'
   elif month in['June','July','August']:
      return 'Summer'
   elif month in ['September','October','November']:
      return 'Autumn'
   else:
      return 'Invalid month'
   
print(check_season('May'))
   
# Write a function called calculate_slope 
# which return the slope of a linear equation
def calculate_scope(x1,x2,y1,y2):
   slope = (y1-y2) / (x1-x2)
   return slope
   
print(calculate_scope(24,10,32,12))
    
# Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic
# equation, solve_quadratic_eqn.
# def quadratic_equation(a,b,c,x):


# Declare a function named print_list.
#  It takes a list as a parameter and 
# it prints out each element of the list
def print_list(llsst):
   for i in llsst:
      print(i)
print(print_list([1,2,3,4,5,6,7,8,"maria",'True']))

# Declare a function named reverse_list. 
# It takes an array as a parameter 
# and it returns the reverse of the array 
# (use loops).
def reverse_list2(arr):
  x = arr[::-1]
  return x
print(reverse_list2([1,2,3,4,5,56,'maria',"kimani"]))

def reverse_list (arr2):
   reversed_arrr =[]
   for i in range(len(arr2)-1,-1,-1):      
       reversed_arrr.append(arr2[i])
       return reversed_arrr
   
arr2 = ["maria",22,2000,"biliionaire"]
print(reverse_list(arr2))

# Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns
#  a capitalized list of items
# def capitalize_list_items(list1):
#    capitalized =[]
#    for i in list1:
#       capitalized.append(i.capitalize())
#     return
      

# print(capitalize_list_items(["maria","Kimani","goretti"]))

# Declare a function named print_list.
# It takes a list as a parameter and 
# it prints out each element of the list.
def print_list(lstt):
   for i in lstt:
      print(i)
    
(print_list(["maria",22,"student","Billionaire"]))
# Declare a function named reverse_list. 
# It takes an array as a parameter and it
#  returns the reverse of the array (use loops).
def reverse_list(arr2):
   reversed =[]
   for i in range(len(arr2)-1,-1,-1):
      reversed.append(arr2[i])
   return reversed
print(reverse_list(["maria",'kimani',"goretti", "beautiful"]))
#   x =arr2[::-1]
#   return  x
# print(reverse_list((["maria","Goretti","Kimani"])))


# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns
#  a capitalized list of items
def capitalize_list_items(lisst):
   y = [l.capitalize() for l in lisst]
   return y
print(capitalize_list_items(["maria","esther","irene","terry","ann","gladys"]))

# Declare a function named add_item.
#  It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(liist,item):
   x=liist.append(item)
   return x
xx =["Maria","goretti","student","billionaire","single"]
print(add_item(xx, "happywoman"))


# Declare a function named sum_of_numbers.
#  It takes a number parameter and it adds
#  all the numbers in that range
def sum_of_numbers(num):
   add = sum(range(1,num+1))
   return add

print(sum_of_numbers(15))


# Declare a function named sum_of_odds. 
# It takes a number parameter 
# and it adds all the odd
#  numbers in that range.
def sum_of_odds(num4):
   x = sum(i for i in range (0,num4+1) if i % 2!=0) 
   return x
print(sum_of_odds(10))

# Declare a function named sum_of_even. 
# It takes a number parameter and 
# it adds all the even numbers in that - range.
def sum_of_even(num5):
   x = sum(xx for xx in range(1,num5+1) if xx %2 ==0)
   return x
print(sum_of_even(20))
      
  
   

   
