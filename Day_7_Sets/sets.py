# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22,24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
It = {"Triggerise","Spen","Mpharma","Basi Go"}
it_companies.update(It)
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Triggerise")
print(it_companies)

# Join A and B
#joins two sets are remves duplicates
C = A.union(B)
print(C)

# Find A intersection B
######### creates a new set with items in set 1 and set 2
D = A.intersection(B)
print(D)

# Is A subset of B
print(A.issubset(B))


# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(A.union(B))
print(B.union(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
# del(A)

# Convert the ages to a set and compare
# the length of the list and the set, which one is bigger?
lst = set(age)
print(lst)



# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
v ="I am a teacher and I love to inspire and teach people"
output = []
for x in v:
    if x not in output:
        output.append(x)
print(output)  