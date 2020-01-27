# ~ available_toppings = ['mushroom', 'cheese', 'pepperoni', 'olives']
# ~ requested_toppings = ['ice-cream', 'mushroom', 'cheese']

# ~ for topping in requested_toppings:
    # ~ if topping in available_toppings:
        # ~ print('Adding ' + topping + ' to your pizza')
    # ~ else:
        # ~ print("Sorry we don't do " + topping)
# ~ print("Finished making your pizza")

#5.9
# ~ usernames = ['Asmita', 'akshya', 'sameer', 'abhash', 'admin']

# ~ if usernames:
    # ~ for user in usernames:
        # ~ if user == 'admin':
            # ~ print("\nHello admin, would you like to see a status report?")
        # ~ else:
            # ~ print("Hello " + user.title() + ". Thanks for logging in again")
# ~ else:
    # ~ print("We need to find some users.")
    
#5.10
current_users = ['Akshya', 'Sameer', 'Abhash', 'Bibhu', 'Bishal']

    
new_users = ['AKSHYA', 'SAmeer', 'raju', 'Ram']

for user in current_users:
    for new in new_users:
        if new.lower() == user.lower():
            print("Username not available")
        else:
            print("Available")
            
#5.11

my_numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in my_numbers:
    if number == 1:
        ordinal = 'st'
    elif number == 2:
        ordinal = 'nd'
    elif number == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    print(str(number) + ordinal)


