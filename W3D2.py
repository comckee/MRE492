#Cole McKee

Hours = int(input("Please enter the number of hours:"))
RPH = int(input("Please enter the rate per hour:"))

if Hours <= 40:
        pay = Hours * RPH
else:
        pay = (1.5*(Hours - 40))*RPH + 40*RPH
print(pay)
