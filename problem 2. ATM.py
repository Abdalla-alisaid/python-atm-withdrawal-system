#problem 2


balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
activity = input ("Is your card active? (yes/no) ").lower()

if activity != "yes":
    print ("\nYour card is blocked or inactive.")
elif amount <= 0:
    print ("\nInvalid withdrawal amount.")
elif amount > balance:
    print ("\nInsufficient balance.")
elif amount > 1000:
    print ("\nDaily withdrawal limit exceeded.")
else:
    remaining_balance = balance - amount
    print ("\nTransaction Successful! ")
    print (f"Remaining Balance: ${remaining_balance}.")
    
