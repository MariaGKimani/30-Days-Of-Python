# Use for loop to iterate from 
# 0 to 100 and print the sum of all numbers.

count = 0
for i in range(101):
    count +=i
print(count)


# Use for loop to iterate from
# 0 to 100 and print the sum of all 
# evens and the sum of all odds.

even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
