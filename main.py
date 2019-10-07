from credentials import Credentials
from user import User


def create_user(fullname, email, username, password):
    """
    This function creates a new user
    """
    new_user = User(fullname, email, username, password)
    return new_user


def save_new_user(new_user):
    """
    Function to save the new user
    """
    new_user.save_user()


def check_existing_user(username):
    """
    Function that checks if a user already exists
    """
    return User.user_exists(username)


def find_user(username):
    """
    Function that finds a user by username and returns the user
    """
    return User.find_by_username(username)


def create_credentials(account_name, email, username, password):
    """
    Function to create new credentials
    """
    new_credentials = User(account_name, email, username, password)
    return new_credentials


def save_new_credentials(new_credentials):
    """
    Function to save the user new credentials
    """
    new_credentials.save_new_credentials()


def delete_credentials(credentials):
    """
    Function to delete credentials
    """
    credentials.delete_credentials()


def check_existing_credentials(account_name):
    """
    Function that check if credentials exist with that account Name and return a Boolean
    """
    return Credentials.credentials_exists(account_name)


def find_credentials(account_name):
    """
    Function that finds a user's credentials by account Name and returns the credentials
    """
    return Credentials.find_by_account_name(account_name)


def generate_password(username):

    return Credentials.generate_password(username)


def display_accounts():
    """
    Function that returns all the saved accounts
    """
    return Credentials.display_accounts()


def main():
    print("Welcome to Password Locker")
    print("-"*10)

    while True:
        print("Use the short codes to navigate Password Locker:")
        print("su - Sign-up, li - Login, ex - Exit")
        print('\n')
        short_code = input().lower()

        if short_code == 'su':
            print("Sign up to create a Password Locker account")
            print("-"*20)

            print("Enter fullname:")
            fullname = input()

            print("Email Address:")
            email = input()

            print("Username:")
            username = input()

            print("Enter Your Password:")
            password = input()

            save_new_user(User(fullname, email, username, password))
            print('\n')
            print(
                "Welcome {}, your account has successfully been created".format(username))
            print('\n')

        elif short_code == 'li':
            print("Login to your Password Locker account")
            print("-"*20)

            print("Username:")
            search_user = input()
            if check_existing_user(search_user):
                user_find = find_user(search_user)
                print("Enter password:")
                password = input()
                if password == user_find.password:
                    print("Welcome {}, you are logged in!".format(username))
                    print('\n')

                    while True:
                        print("Please use the following short codes:")
                        print("""
                        add - Add & save existing accounts, gen - Generate password for new account,
                        display - display accounts, del - Delete account, lo - Log out
                        """)

                        short_code = input().lower()

                        if short_code == 'add':
                            print('\n')
                            print("Add new account")
                            print("-"*10)

                            print("Account Name:")
                            account_name = input()

                            print("Email Address:")
                            email = input()

                            print("Username:")
                            username = input()

                            print("Password:")
                            password = input()
                            save_new_credentials(Credentials(
                                account_name, email, username, password))
                            print('\n')
                            print(
                                "Your {} account has successfully been added!".format(account_name))
                            print('\n')

                        elif short_code == 'gen':
                            print('\n')
                            print(
                                "A random password will be created for this account")
                            print("-"*30)

                            print("Account Name:")
                            account_name = input()

                            print("Email Address:")
                            email = input()

                            print("Username:")
                            username = input()
                            password = generate_password(username)
                            print("\n Your password is {} for the account {}".format(password,username))
                            save_new_credentials(Credentials(
                                account_name, email, username, password))
                            print('\n')
                            print(
                                "Your {} account has successfully been added!".format(account_name))
                            print('\n')

                        elif short_code == 'display':
                            if display_accounts():
                                print('\n')
                                print("Here is a list of all your accounts")
                                print('\n')

                                for credentials in display_accounts():
                                    print(
                                        "Account name:{} \n Email: {} \n username: {} \n password: {}".format(credentials.account_name, credentials.email, credentials.username, credentials.password))
                                    print('\n')
                            else:
                                print('\n')
                                print(
                                    "You do not have any contacts saved yet")
                                print('\n')
# delete function error
                        elif short_code == 'del':
                            print('\n')
                            print(
                                "What is the name of the account you want to delete?")
                            account_name = input()
                            if find_credentials(account_name):
                                # delete_credentials =  input()
                                # for credentials in credentials_list:
                                #   if credential==input():
                                    
                                #   else:
                                #     print('No account by that name')
                                  
                                print('\n')
                                print(
                                    "Your {} account has been deleted successfully!".format(account_name))
                                print('\n')

                        elif short_code == 'lo':
                            print('\n')
                            print("You have logged out successfully!")
                            print('\n')
                            break

                        else:
                            print('\n')
                            print(
                                "Use the provided short code to navigate the password locker")
                            print('\n')

                    else:
                        print("Incorrect password")
                        print('\n')

                else:
                    print("{} does not exist, please sign up.".format(username))
        elif short_code == 'ex':
            print("\n")
            print("Exiting...")
            print("\n")
            # break
        else:
            print("Use the provided short code to navigate the password locker")


if __name__ == '__main__':
    main()
