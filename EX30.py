# Markhus Dammar
# 10/7/19
# This program practices else, if, and elif

people = 30
cars = 40
trucks = 15
# Hi I like puppies

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's jut take the trucks.")
else:
    print("Fine, let;s stay hine then.")
