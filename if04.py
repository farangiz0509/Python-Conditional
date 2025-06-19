price = 100 
age = int(input("enter your age:"))

print(age)

discount = 0

if age < 7:
    discount = 50
if age >= 7 and age < 17:
    discount = 20
if age > 60:
    discount = 30
    
discount = (discount / 100) * price
main_price = price - discount

if discount > 0:
    print(f"main_price:{main_price} som{discount}% used discount ")
    
else: 
    print(f"main_price:{main_price} som ")
    