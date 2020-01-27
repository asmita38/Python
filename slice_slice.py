players = ["Asmita", "utsav", "sameer", "akshya"]
print(players[0:3])

for player in players[1:]:
    print(player.title())
print("\n")

#copying a list
my_foods = ["pizza", "momo", "brownie"]
friends_foods = my_foods[:]     #copying the whole list
friends_foods.insert(1,"icecream")
print("My favorite foods are: ",my_foods)
print("My friend's favorite foods are: ",friends_foods)
