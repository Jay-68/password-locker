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
