#tuples are immutable and defined with parenthesis

dimensions = (200, 50)
print(dimensions[0])

# ~ dimensions[1] = 300 #shows error

#writing over a tuple
print("original dimensions: ")
for dimension in dimensions:
    print(dimension)
print("\n")
dimensions = (400,78)
print("new dimensions: ")
for dimension in dimensions:
    print(dimension)
print("\n")
    
#4.13
buffet_foods = ("rice", "chicken", "daal", "saag")
for food in buffet_foods:
    print(food)
# ~ buffet_foods[0] = ("curry")
print("\n")



