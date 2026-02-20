age = 21

print(age)

# print("you are " + age + " years old") #This isn't right. We should make "TYPE CASTING".

print ("you are " + str(age) + " years old") # TYPE CASTING
print ("you are" , age,"years old") # We got delete the spaces before and after the strings. 
print (f"you are {age} years old") # This called "f-string" COMMONLY USE

# Data Types

#INTEGER

age =21
players = 2
quantity = 5 

print(f"You are {age} years old")
print (f"there are {players} players online")

# FLOATS

gpa=3.2
distance= 2.5
price=10.99

print(f"your gpa is {gpa}")

#STRING

name = "MYM"
food = "pizza"
email= "mym@phyton.com"

print(f"Hello {name}")


#BOOLEAN

online = True
for_sale = False
running = False

print (f"Are you online?: {online}")

if running:
    print ("the game is running")
else:
    print("the game is not running")
