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
        self.new_credential=Credentials("tweeter","juru-juliette","@tweetiii")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"tweeter")
         self.assertEqual(self.new_credential.password,"juru-juliette")
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
        Credentials.credential_list = []
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''    
        self.new_credential.save_credential()
        test_credential = Credentials("tweeter","juru-juliette","@tweetiii")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential=Credentials("tweeter","juru-juliette","@tweetiii")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1) 
    def test_find_credential_by_name(self):
        '''
        test to check if we can find a credential by account name and dispaly information
        '''     
        self.new_credential.save_credential()
        test_credential=Credentials("tweeter","juru-juliette","@tweetiii")
        test_credential.save_credential()

        found_credential=Credentials.find_by_name("tweeter")

        self.assertEqual(found_credential.password,test_credential.password)
 

if __name__=='__main__':
    unittest.main()        
