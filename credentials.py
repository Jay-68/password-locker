import random
import unittest

class Credentials:
    '''
    This class creates new instances of the class Credentials
    '''

    def __init__(self, account_name, email, username, password):
        self.account_name = account_name
        self.email = email
        self.username = username
        self.password = password

    credentials_list = []

    def save_credentials(self):
        '''
        Saves user credentials to the credentials_list
        '''
        Credentials.credentials_list.append(self)

    @classmethod
    def credentials_exists(cls, account_name):
        '''
        Checks if there is an already existing account
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
            else:
                return False

    def delete_credentials(self):
        '''
        deletes an existing profile
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_accounts(cls):
        '''
        Displays the credentials of a username
        '''
        return cls.credentials_list

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method that takes in an account name and returns the credentials that match that account name.
        Args:
            account_name: Account name to search for
        Returns :
            Full credentials that matches the account_name.
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def generate_password(cls, username):
        '''
        This method generates a random password for a new user profile
        '''
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        generate_password = ''
        for c in range(10):
            generate_password += random.choice(chars)
        print(generate_password)

        # letters = username[1:4]
        # number_1 = str(random.randint(0, 9))
        # number_2 = str(random.randint(9, 16))
        # gen_pass = '@'+number_1+letters+number_2+'!'
        # letters.upper()
        # return gen_pass


if __name__ == '__main__':
    unittest.main()
