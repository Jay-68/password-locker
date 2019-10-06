class User:
    '''
    This class generates new user instances
    '''

    def __init__(self, fullname, email, username, password):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password

    user_list = []

    def save_user(self):
        '''
        This method saves new created user objects into user list
        '''
        User.user_list.append(self)

    @classmethod
    def user_exists(cls, username):
        '''
        Checks if the user exists in the user list.
        Args:
        username:username to search if the user already exists and returns a boolean, True or False.
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
            else:
                return False

    @classmethod
    def find_by_username(cls, username):
        '''
        Finds a user depending on if the user already exists
        '''
        for user in cls.user_list:
            if user.username == username:
                return user
            else:
                return 0
