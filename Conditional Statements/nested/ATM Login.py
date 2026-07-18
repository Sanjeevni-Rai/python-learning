pin = int(input("Enter PIN: "))

if pin == 1234:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 5000:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")