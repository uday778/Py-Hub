age=input("enter your age :  ")
ageint=int(age)
day="wednesday"

price=12 if ageint>=18 else 8
if day=="wednesday":
    price=price-2


print("ticket price $" ,price)