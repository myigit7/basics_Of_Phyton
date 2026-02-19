age = int(input("Enter your age"))

if age >= 65:
    print ("You should not drive a car")
elif age >= 18:
    print("You can signed up!")
elif age < 0:
    print ("You have not born yet")
else:
    print("You must be 18+ to sign up!")


for_sale = True

if for_sale:
    print ("You can sale!")
else:
    print ("Ypu can not sale!")