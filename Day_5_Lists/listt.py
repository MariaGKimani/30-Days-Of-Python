# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])

# Add the min age and the max age again to the list
x = min(ages)
print(x)
y = max(ages)
print(y)

z = (19,26)
ages.extend(z)
print(ages)

# Find the median age 
# (one middle item or two middle items divided by two)
x= len(ages) // 2
y =ages[x]
print(y)
# Find the average age
# (sum of all items divided by their number )
avg = sum(ages) /len(ages)
print(avg)

# Find the range of the ages(max minus min)
def minmax(ages):
    min_val = min(ages)
    max_val = max(ages)

    return (min_val, max_val)
print(minmax([19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]))

# Compare the value of (min - average) and (max - average), use abs() method
p= abs(min(ages) - avg)
print(p)

q = abs(max(ages) -avg)
print(q)

