import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_credential=Credentials("tweeter","@tweetiii")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"tweeter")
        self.assertEqual(self.new_credential.password,"@tweetiii")
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into credential list
        '''
        self.new_credential.save_credential()   
        self.assertEqual(len(Credentials.credential_list),1) 

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []
if __name__=='__main__':
    unittest.main()        
