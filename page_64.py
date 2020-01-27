# ~ #4.3
# ~ for value in range(1,21):
    # ~ print(value)
# ~ print("\n")

# ~ #4.4

# ~ numbers = list(range(1,1000001))
# ~ print("minimum no. is: ",min(numbers))
# ~ print("maximum no. is: ",max(numbers))
# ~ print("sum of the numbers is: ",sum(numbers), "\n")

# ~ #4.6
# ~ odd_numbers = list(range(1,20,2))
# ~ for odd in odd_numbers:
    # ~ print(odd)

#4.7
multiples_of_3 = list(range(3,31,3))
for multiples in multiples_of_3:
    print(multiples)

#4.8
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes,"\n")

#4.9
cubes = [value**3 for value in range(1,11)]
