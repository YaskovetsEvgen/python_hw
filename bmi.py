a = float(input("weight,kg:"))
b = float(input("height,m:"))
# calculation BMI
c = (a/(b**2))
# output scale
d = float(c-20)
e = float(50-c)
print("20" + round(d)*"=" + "|" + round(e)*"=" + "50")