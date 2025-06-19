balance = 5000.0

input = float(input("how much do you want to get"))

if input >= 0 :
    if input <= balance :
        print(f"money was taken. left :{balance} som")
    else :
        print("money is not enough. your balance {balance}som")
