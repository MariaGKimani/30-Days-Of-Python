# Create an empty tuple

tpl =()
tpl =tuple()
print(type(tpl))

# Create a tuple containing names of your sisters 
# and your brothers (imaginary siblings are fine)

brothers = ("Joseph","Tito","Steve",)
sisters =("Esther","Irene","Terry","Gladys","Ann")

siblings = brothers+ sisters
print(siblings)
# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add
# the name of your father and mother and assign it to family_members

family_members = siblings + ("Elizabeth","Paul")
print(family_members)

parents = ("Elizabeth","Paul")


fruits =("Apple","Mango","Orange","Banana")
vegetables =("SukumaWiki","cucumber","codjet","pepper")
animal_products =("Milk","meat")
food_stuff_tp =(fruits + vegetables + animal_products)
print(food_stuff_tp)
food_stuff_lt = tuple(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the
# food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_lt)//2)


# Slice out the first three items and the 
#last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])


# Delete the food_staff_tp tuple completely
del food_stuff_tp
print(food_stuff_lt)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

/////