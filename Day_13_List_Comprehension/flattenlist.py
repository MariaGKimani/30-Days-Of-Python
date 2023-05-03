# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for row in list_of_lists for numbers in row for number in numbers]
print(flattened_list)


list_list=[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]
flattened_lists = []
for sublist in list_of_lists:
    for x in sublist:
        for i in x:

            flattened_lists.append(i)
print(flattened_list)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

#  expected output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

flattened_countries = []
for country in countries:
    for county in country:
        flattened_countries.append(county)
print(list(flattened_countries))