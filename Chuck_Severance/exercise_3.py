hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter your rate per hour:")
r = float(rate)


if (h > 40):
   # print("Overtime")
    reg = h * r
    otp = (h - 40.0) * (r * 0.5)
   # print (reg, otp)
    xp = reg + otp
else:
   # print("Regular")
    xp = h * r
print ("Pay:", xp)