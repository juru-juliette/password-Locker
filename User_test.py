import unittest # Importing the unittest module
from UserAcc import UserAcc # Importing the contact class
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = UserAcc("Juliette","k@yly123","k@yly123") # create user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.Username,"Juliette")
        self.assertEqual(self.new_user.Password,"k@yly123")
        self.assertEqual(self.new_user.confirm_pswd,"k@yly123")
####################################################################FIRST STEP
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(UserAcc.user_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            UserAcc.user_list = []
####################################################################SECOND STEP

if __name__ == '__main__':
    unittest.main()