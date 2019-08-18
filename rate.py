hours = input("enter the hours")
rate = input("enter the rate")
hours = int(hours)
rate = int(rate)
pay = rate*hours
if hours > 40:
    pay = pay + 0.5*(hours-40)*10
print (pay)

