#4.10
favourite_people = ["Mummy", "Daddy", "Mikey", "Akshya", "Abhash", "Sameer", "Ashmita"]
l = int(len(favourite_people))

first_three = favourite_people[:3]
middle_three = favourite_people[int(l/2):(int(l/2)+ 3)]
last_three = favourite_people[-3:]

print(first_three)
print(middle_three)
print(last_three)
print("\n")

#4.11
my_pizzas = ["mushroom", "chicken", "pepperoni"]
friends_pizzas = my_pizzas[:]
print("my favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)
print("\n")
friends_pizzas.append("ham")
print("my friend's favorite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza)
