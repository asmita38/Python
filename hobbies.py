hobbies = ["dancing", "singing", "painting"]
# ~ print("I like " + hobbies[0].title())
# ~ print("I like " + hobbies[1].title())

# ~ vehicles = ["car", "bike", "plane"]
# ~ print("I would like to own a " + vehicles[0] + "\nbut right now i just have a " + vehicles[1])
# ~ hobbies.append("eating") #to add to the list
# ~ print(hobbies)

# ~ hobbies.insert(1, "sleeping")   #inserting at an index
# ~ print(hobbies)

# ~ del hobbies[0]
# ~ print(hobbies)  #deleting from an index

popped_item = hobbies.pop() #pop the last item
print(hobbies)
print(popped_item)

new_pop = hobbies.pop(0)    #pop from an index
print(new_pop)

skin_care = ["cream", "sheet masks", "body wash", "scrub"]
too_expensive = "sheet masks"
skin_care.remove(too_expensive) #removing an item directly
print(skin_care)
