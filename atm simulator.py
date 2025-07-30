balance=int(input("enter balance:"))
print(" WELCOME TO ATM")
print("1. Check balance")
print("2. Withdraw amount")
print("3. exit.")

choice = input("enter your choice (1,2,3): ")
if choice== '1':
    print("Your balance is :",balance)
elif choice=='2':
    amount=float(input("enter amount to withdraw:"))
    if amount <= balance:
        balance-=amount
        print("please collect your cash",amount)
        print(" your Remaining balance is:",balance)
    else:
        print("Insuffient balance.")
elif choice=='3':
    print("Thank you visit again.")
else:
    print("invalid choice.")