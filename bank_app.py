users = {}
all_users =[{'user_email': 'r', 'password': 'f', 'balance': 0}, {'user_email': 'a', 'password': 'a', 'balance': 0}]
user_input = input("Press 1: create account\nPress 2: transaction \n")
# while int(user_input) != 1:
if int(user_input) == 1:
    while int(user_input) == 1 :
        user_email = input("enter your email address\n")
        #check if the email exits in the data
        all_userid = [x['user_email'] for x in all_users]
        print(all_userid)
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
        users['balance'] = 0
        all_users.append(users)
        print(f"Dear {user_email} your account has be created successfully")
        print(all_users)
        user_input = input("Press 1: create account\nPress 2: transaction \n")
elif int(user_input) == 2:
    while int(user_input) == 2 :
        user_email = input("enter your email address\n")
        all_userid = [x['user_email'] for x in all_users]
        if user_email not in all_userid:
            print("invalid email")
            user_email = input("enter your email address\n")
        user_password = input("enter your password\n")
        # all_userid = [x['user_email'],y['password'], for x in all_users if user_email == ]
        for user in all_users:
            if user_email == user['user_email'] and  user_password == user['password']:
                print('seen')
                break
else:
    user_input = input("Press 1: create account\nPress 2: transaction \n")
        

    


    


