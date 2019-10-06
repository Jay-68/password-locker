import unittest
from user import User


class test_user(unittest.TestCase):
    '''
    This test class defines test cases for the behavior of the User class.
    '''

    def setUp(self):
        '''
        The set up method to run each test case.
        '''
        self.new_user = User(
            'James Ngari', 'ngari.james.n@gmail.com', 'Jay-68', '123456')

    def test_init(self):
        '''
        This test checks if the new user has been initialized with the parameters in the class User.
        '''
        self.assertEqual(self.new_user.fullname, 'James Ngari')
        self.assertEqual(self.new_user.email, 'ngari.james.n@gmail.com')
        self.assertEqual(self.new_user.username, 'Jay-68')
        self.assertEqual(self.new_user.password, '123456')

    def tearDown(self):
        '''
          The test case method cleans up after each test has been run
          '''
        User.user_list = []


if __name__ == '__main__':
    unittest.main()
