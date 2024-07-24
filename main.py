def show_balance():
    print(f'your balance is ${balance}')

def deposit():
    global balance
    amount = float(input('enter amount to deposit: '))
    
    if amount < 0:
        print("cant deposit negative money")
    else:
        balance += amount

def withdraw():
    global balance
    amount = float(input('enter amount to withdraw: '))

    if amount > balance:
        print('insufficient balance')
    elif amount < 0:
        print('amount cant be negative')
    else:
        balance -= amount


balance = 0
is_running = True

while is_running:
    print("bank")
    print("1.show balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

    choice = input('enter your choice (1-4): ')

    match choice:
        case '1':
            show_balance()
        case '2':
            deposit()
        case '3':
            withdraw()
        case '4':
            is_running = False
        case _:
            print("invalid choice. try again.")

print('thank you for using this bank.')