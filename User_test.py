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
        self.new_user = UserAcc("Juliette","k@yly123") # create user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.Username,"Juliette")
        self.assertEqual(self.new_user.Password,"k@yly123")
####################################################################FIRST STEP