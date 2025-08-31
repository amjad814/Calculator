balance = 10000      # initial balance

pin = "0112"        # defualt pin

print("======== Welcome TO Simple ATM")

user_pin = input("Enter your pin : ")
if user_pin == pin:
    while True:
        print("/n ----ATM manue-----")
        print("1. check money")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice =input("Enter your choice 1-4 : ")
        if choice == "1":
            print(f"your current balance is:{balance} Rs")

        elif choice == "2":
            amount = int(input("Enter amount to deposit:"))
            balance += amount
            print(f" {amount} PKR deposit successfully.")
            print(f"New balance is:{balance} PKR")
        elif choice == "3":
          amount = int(input("Enter amount to withdraw:"))
          if amount <= balance: 
              balance -= amount
              print(f" {amount} PKR withdraw  successfully.")
              print(f"Remaining  balance is:{balance} PKR")
          else:
              print("insufficiant ballance")
        elif choice =="4":
              print("thankyou for using our ATM. GoodBuy!")
              break
        else:
            print("invelid option. please try again")
else:
    print(" incorrect pin . access denied")





