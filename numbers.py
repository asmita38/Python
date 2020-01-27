numbers = list(range(1,6))
print(numbers)

for number in range(1,6):
    print(number)
print("\n")

#even_numbers
for num in range(2,11,2):
    print(num)
print("\n")

#squares
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares,"\n")


#list_comprehension

squares = [value**2 for value in range(1,11)]
print(squares)

