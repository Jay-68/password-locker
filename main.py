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
