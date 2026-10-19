def computepay(h, r):
    if (h >40):
        reg = h * r
        otp = (h - 40.0) * (r * 0.5)
        xp = reg + otp
    else:
        xp = h * r
    return xp

hrs = input("Enter Hours:")
hflo = float(hrs)
rate = input("Enter Rate:")
rflo = float(rate)
p = computepay(hflo, rflo)
print("Pay", p)