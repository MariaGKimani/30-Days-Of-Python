#  Iterate 0 to 10 using for loop
for i in range (11):
    print(i)


# Iterate 10 to 0 using for loop
for i in range(10,-1 ,-1):
    print(i)



# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

# for i in range(1,8):
#     print("#" *i)

# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for j in range (8):
        print("#",end="")
    print()

# Write a program to construct the following pattern using nested loops
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *



# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range (11):
    print(f"{i}*{i}= {i*i}")

# Iterate through the list, 
# ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.

languages = ['Python','Numpy','Pandas','Django','Flask']
for language in languages:
    print(language)


# Use for loop to iterate from
#  0 to 100 and print only even numbers
for i  in range (0, 101, 2):
    print(i)


#Use for loop to iterate from
#0 to 100 and print only odd numbers
for i in range(0,101,3):
    print(i)

