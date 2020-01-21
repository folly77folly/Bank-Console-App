users = {}
all_users =[
    {'user_email': 'ab@gmail.com', 'password': 'pass', 'balance': 10.0}, 
    {'user_email': 'cd@gmail.com', 'password': 'pass', 'balance': 0.0}
]
user_input = input("Press 1: create account\nPress 2: transaction \n").strip()
def call():
    user_input = input("Press 1: create account\nPress 2: transaction \n")
while user_input == str(1) :
    user_email = input("enter your email address\n")
    #check if the email exits in the data
    all_userid = [user['user_email'] for user in all_users]
    # print(all_userid)
    while user_email in all_userid:
        print("the email already exsits !!!")
        user_email = input("enter another email address\n")
    user_pass = input("enter your password\n")
    user_confirm_pass = input("confirm your password\n")
    while user_pass != user_confirm_pass :
        print("your passwords don't match")
        user_pass = input("enter your password\n")
        user_confirm_pass = input("confirm your password\n")
    #save user to database
    users = {}
    users['user_email'] = user_email
    users['password'] = user_pass
    users['balance'] = 0.0
    all_users.append(users)
    print(f"Dear {user_email} your account has be created successfully")
    user_input = input("Press 1: create account\nPress 2: transaction \n")

while user_input == str(2) :
    user_email = input("enter your email address to login:\n")
    all_userid = [x['user_email'] for x in all_users]
    if user_email not in all_userid:
        print("invalid email address try again !")
        user_input =''
        user_input = input("Press 1: create account\nPress 2: transaction \n").strip()
    else:
        user_password = input("enter your password :\n")
    registered_user = [user for user in all_users if user_email == user['user_email'] and  user_password == user['password']]
    while registered_user :
        user_transaction = input("Press 1: check balance\nPress 2: deposit \nPress 3: withdrawal\nPress 4: transfer \nPress 5: logout \n")
        while user_transaction == str(1):
            balance = float(registered_user[0]['balance'])
            print(f'your balance is {balance}\n')
            break
        while user_transaction == str(2):
            deposit_amt = input('enter amount to deposit :\n')
            balance = registered_user[0]['balance']
            new_balance = float(deposit_amt) + balance
            registered_user[0]['balance'] = new_balance
            print(f'deposit made sucessfully your balance is now {new_balance}\n')
            break
        while user_transaction == str(3):
            withdrawal_amt = float(input('enter amount to withdraw :\n'))
            balance = float(registered_user[0]['balance'])
            if balance < withdrawal_amt:
                print('insufficent balance')
                break
            else:
                new_balance = balance - withdrawal_amt
                registered_user[0]['balance'] = new_balance
                print(f'you have withdrawn {withdrawal_amt} and your balance is {new_balance}')
                break
        while user_transaction == str(4):
            benficiary_email = input('enter benficiary email\n')
            balance = float(registered_user[0]['balance'])
            benficiary_user = [user for user in all_users if benficiary_email == user['user_email']]
            if benficiary_user:
                if benficiary_user[0]['user_email'] == registered_user[0]['user_email']:
                    print('you cannot transfer to yourself')
                    break                
                transf_amt = float(input('enter amount to transfer\n'))
                benficiary_balance = float(benficiary_user[0]['balance'])
                if balance < transf_amt:
                    print('Insufficent balance')
                    break
                else:
                    new_balance = balance - transf_amt
                    updated_balance =  benficiary_balance + transf_amt
                    registered_user[0]['balance'] = new_balance
                    benficiary_user [0]['balance'] = updated_balance
                    print('transfer made successfully\n')
                    print(f'your balance is {new_balance} your beneficary balance is now {updated_balance}\n')
                    break
            else:
                print('Invalid benefinary email try again')
                break
        if user_transaction == str(5):
            print(f"thank you {registered_user[0]['user_email']} for banking with us\n")
            registered_user = None
            exit()
