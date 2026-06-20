import json
AdminAccount="Leon Miles"
AdminPassword="TON618Leon"
user_info=""
user_password=""
def load_info():     #loads in the data from the file
    try:
        with open("user_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {} 

def initiate_program():    #loads info and puts it into user_info
    load_info()
    user_info=load_info()

initiate_program()

def save_info(user_info, user_name, user_password): #saves all information
    user_info[user_name] = user_password
    with open("user_data.json", "w") as file:
        json.dump(user_info, file, indent=4)

def view_all_info(user_info):    #shows all user information
    print("\n--- ALL REGISTERED USERS ---")
    for user_name, user_password in user_info.items():
        print(f"User: {user_name} | Password: {user_password}")

def username_data_queerie(user, user_info): #checks username exists in database
    if user in user_info:
        return True
    else:
        return False

def view_one_user(user_info):    #view one user
    user = input("Who do you want to view: ")
    if username_data_queerie(user, user_info) is True:
        password = user_info[user]  # Safely grabs the password from user_info
        print(f"User: {user} | Password: {password}")
    else:
        print("That user does not exist.")

def delete_user_data(user_info):    #deleting user function
    det = False
    option = input("Enter 'user' to delete one user, 'all' to delete all, or 'cancel': ")
    while det is False:
        det = True
        
        if option == "user":
            account = input("Which user do you want to delete: ")
            
            if account not in user_info:
                print("That user does not exist.")
                continue
                
            confirm = input("Are you sure you want to delete this user? yes or no: ")
            cont = False
            while cont is False:
                if confirm == "yes":
                    del user_info[account]
                    with open("user_data.json", "w") as file:
                        json.dump(user_info, file, indent=4)
                    print("Account Terminated!")
                    cont = True
                elif confirm == "no":
                    cont = True
                    print("Termination canceled")
                else:
                    confirm = input("Please confirm yes or no: ")
        elif option == "cancel":
            print("Request canceled")
            det = True
        elif option == "all":
            code = input("Please enter the override code to delete all data: ")
            if code == "AdminTerminationCode":
                confirm = input("Are you sure you want to delete all the data? yes or no: ")
                absol = False
                while absol is False:
                    if confirm == "yes":
                        absol = True
                        user_info.clear() 
                        with open("user_data.json", "w") as file:
                            json.dump({}, file)
                        print("System data reset")
                    elif confirm == "no":
                        absol = True
                        print("Data reset canceled")
                    else:
                        confirm = input("Please confirm yes or no: ")
            else:
                print("Access denied")
                det = True
        else:
            det = False
            option = input("Please select all, user or cancel: ")

def choose_option_admin(user_info):    #admin controls
    all_done = False
    while all_done is False:
        choice = input("\nWould you like to logout, close the app, view user data, delete someone's account or change password? logout, view, delete, change or close: ")
        
        if choice == "view":
            howmany = input("Would you like all data, cancel or one person's data? all, cancel or one: ")
            jim = False
            while jim is False:
                if howmany == "all":
                    view_all_info(user_info)
                    jim = True
                elif howmany == "one":
                    view_one_user(user_info)
                    jim = True
                elif howmany == "cancel":
                    jim = True
                else:
                    howmany = input("Please select all, cancel or one: ")
        
        elif choice == "delete":
            delete_user_data(user_info)
                
        elif choice == "logout":
            print("Exiting Admin Panel.")
            all_done = True
        elif choice=="close":
            all_done=True
            return "shutdown"
        else:
            print("Invalid admin option.")
            all_done=input("Select logout,close,delete or view")

def password_check(user_password):  #checks for password being adequate
    if len(user_password) <8 or user_password.islower() or user_password.isupper():
        return False
    else:
        return True

def sign_up(user_info):    #sign up function
    user_name=input("Choose your user name:")
    while username_data_queerie(user_name,user_info) is True:
        user_name=input("That user name is already taken please select another one:")
    user_password=input("Please choose a password that is at least 8 characters long and has both lower and upper case letters")
    while password_check(user_password) is False:
        user_password=input("That password is not adequate. Please try again:")
    print("You have been signed in!")
    save_info(user_info, user_name, user_password)
    return user_name,user_password

def user_password_data_queerie(user_info,user_password,user_name):       #checks password matches user
    if user_info[user_name]==user_password:
        return True
    else:
        return False

def login(user_info):  #login function
    user_name=input("Please enter your user name:")
    while username_data_queerie(user_name,user_info) is False:
        user_name=input("That user name was not found. Please try again:")
    user_password=input("Enter your user password:")
    while user_password_data_queerie(user_info,user_password,user_name) is False:
        user_password=input("Password incorrect please try again")
    print("You have been logged in")
    return user_name, user_password

def admin_login(user_info,AdminAccount,AdminPassword):
    Auser=input("What is the admin user name:")
    if Auser!=AdminAccount:
        print("Access denied")
        return False
    else:
        Apass=input("What is the admin password:")
        if Apass!=AdminPassword:
            print("Access denied!")
            return False
        else:
            print("Access granted to admin account")
            return True


def user_entry_options():    #main menu
    entry_dynamic=False
    opt=input("Would you like to sign up for a new account, login to access your current account, close to shut down the app or admin to access your administrator account:")
    while entry_dynamic is False:
        entry_dynamic=True
        if opt=="sign up":
            print("Initiating sign up!")
            return 1
        elif opt=="login":
            print("Initiating login process")
            return 2
        elif opt=="admin":
            print("Initiating administrator process")
            return 3
        else:
            entry_dynamic=False
            opt=input("Please type in sign up, login or admin:")

user_info=load_info()

def process(user_info,user_name,user_password):
    entry_option=user_entry_options()
    if entry_option==1 or entry_option==2:
        if entry_option==1:
            sign_up(user_info)
        else:
            login(user_info)
        nvm=choose_option_user(user_info,user_name,user_password)
        if nvm=="shutdown":
            return "shutdown"
    elif entry_option==3:
        if admin_login(user_info,AdminAccount,AdminPassword) is False:
            print("JIIM")
        else:
            closing=choose_option_admin(user_info)
            if closing=="shutdown":
                return "shutdown"
    else:
        return "shutdown"

def delete_account(user_info,user_name,user_password):
    confirmation=input("Are you sure you want to delete your account!? yes or no")
    conf=False
    while conf is False:
        conf=True
        if confirmation=="yes":
            del user_info[user_name]
            print("Account deleted!")
            return True
        elif confirmation=="no":
            print("Deletion canceled!")
        else:
            conf=False
            confirmation=input("Please confirm yes or no to delete your account")

def choose_option_user(user_info,user_name,user_password):
    user_choice=input("Would you like to logout, close app, delete account or change password:")
    rvn=False
    while rvn is False:
        if user_choice=="logout":
            rvn=True
            print("Logging out!")
        elif user_choice=="close":
            rvn=True
            return "shutdown"
        elif user_choice=="delete":
            shut=delete_account(user_info,user_name,user_password)
            rvn=shut

user_name=""

infinity=False
while infinity is False:
    close=process(user_info, user_name ,user_password)
    if close=="shutdown":
        infinity=True
        print("App shutting down!")
        

