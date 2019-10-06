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
