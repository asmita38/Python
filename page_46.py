# 3.4
guest_list = ["Sameer", "Akshya", "Abhash", "Mikey"]

print("Hello " + guest_list[0] + "!.I would like to invite you to my party")
print("Hello " + guest_list[1] + "!.I would like to invite you to my party")
print("Hello " + guest_list[2] + "!.I would like to invite you to my party")
print("Hello " + guest_list[3] + "!.I would like to invite you to my party")

#3.5
print(guest_list[0] + "can't make it")
guest_list.remove("Sameer")
print("New guest list: ",guest_list)

#3.6
print("Guys! I have a good news. I found a bigger table.")
guest_list.insert(0, "Mummy")
guest_list.insert(-1, "Daddy")
guest_list.append("Utsav")

for guest in guest_list:
    print("hello ", guest)
