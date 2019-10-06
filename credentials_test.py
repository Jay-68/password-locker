import unittest
from credentials import Credentials

class test_credentials(unittest.TestCase):
    '''
    This test class defines the test cases for the credentials class.
    '''

    def setUp(self):
        '''
        Set up method for each test cases in the credentials class
        '''
        self.new_credentials = Credentials(
            'facebook', 'face@email.com', 'James', '123qwerty')

    def test_init(self):
        self.assertEqual(self.new_credentials.account_name, 'facebook')
        self.assertEqual(self.new_credentials.username, 'James')
        self.assertEqual(self.new_credentials.email, 'face@email.com')
        self.assertEqual(self.new_credentials.password, '123qwerty')

    def tearDown(self):
        '''
        The test case method cleans up after each test has been run
        '''
        Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
        This tests if the new credentials are added into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == '__main__':
    unittest.main()
