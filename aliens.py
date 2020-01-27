#5.5

# ~ alien_color = ['blue', 'yellow', 'green']
# ~ print("The colors of aliens are:")
# ~ for alien in alien_color:
    # ~ print(alien)

# ~ shot_alien = input("\nEnter the color of alien you want to shoot: ")

# ~ if (shot_alien == 'green'):
    # ~ points = 5
# ~ elif (shot_alien == 'red'):
    # ~ points = 10
# ~ elif (shot_alien == 'blue'):
    # ~ points = 20
# ~ print("Congratulations! you earned " + str(points) + " points")

#5.6
age  = int(input  ("Enter your age: "))


if age < 2:
    stage = 'baby'
elif (age == 2) or (age < 4):
    stage = 'toddler'
elif (age == 4) or (age < 13):
    stage = 'kid'
elif (age == 13) or (age < 20):
    stage = 'teenager'
else:
    stage == 'adult'


if stage in 'aeiou':
    print(stage)

# ~ if (stage[0] in vowels):
    # ~ print("you are an " + stage)
# ~ else:
    # ~ print("you are a " + stage)
    
