password = input("enter password:")

number = ("0" in password or "1" )
letter = ("A" in password or "a")

if len(password) >= 8 and number and letter:
    
    print("password is true")
else:
    print(" your password is incorrect it should include 1 number and 1 letter")
