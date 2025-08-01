import datetime
balance = 0
transactions = []
current_pin = "1234"
while True:
    print("Welcome to the ATM")
    print("Insert your card here")
    pin = input("Enter your PIN: ")
    if pin == current_pin:
        print(''' 
            1. Deposit
            2. Withdraw
            3. Balance Enquiry
            4. PIN Change
            5. Exit
                ''')
        option = int(input("Select any one of the options: "))
        if option == 1:
            amount_input = input("Feed the cash: ")
            if not amount_input.isdigit():
                print("Invalid input. Please enter a valid integer amount.")
                continue
            amount = int(amount_input)
            if amount % 100 == 0:
                print("Cash accepted")
                balance += amount
                transactions.append({
                    'amount': amount,
                    'type': 'Deposit',
                    'datetime': datetime.datetime.now()
                })
                print(f"Deposit successful! New balance: {balance}")
            else:
                print("Please enter the amount in multiples of 100")
        elif option == 2:
            amount_input = input("Enter the amount to withdraw: ")
            if not amount_input.isdigit():
                print("Invalid input. Please enter a valid integer amount.")
                continue
            amount = int(amount_input)
            if amount <= balance:
                print("Collect your cash")
                balance -= amount
                transactions.append({
                    'amount': -amount,
                    'type': 'Withdraw',
                    'datetime': datetime.datetime.now()
                })
                print(f"Withdrawal successful! New balance: {balance}")
            else:
                print("Insufficient funds")
        elif option == 3:
            now = datetime.datetime.now()
            print(f"Date: {now.strftime('%Y-%m-%d')}    Time: {now.strftime('%H:%M:%S')}")
            print(f"Your current balance is: {balance}")
            print("Transaction History:")
            if transactions:
                for t in transactions:
                    dt = t['datetime'].strftime('%Y-%m-%d %H:%M:%S')
                    print(f"{t['type']}: {t['amount']} at {dt}")
            else:
                print(" No transactions yet")
        elif option == 4:
            new_pin = input("Enter your new PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                current_pin = new_pin
                print("PIN changed successfully")
            else:
                print("PIN must be 4 digits")
        elif option == 5:
            print("Thank you for using the ATM. Goodbye!")
            break
    else:
        print("Incorrect PIN. Please try again.")