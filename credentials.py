class Credentials:
    '''
    class that generates new instance for credentials
    '''
    credential_list=[]
    def __init__(self,account_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New credential account name.
            password : New credential password.
        '''
        self.account_name = account_name
        self.password = password

    credential_list=[]
    def save_credential(self):
        
        '''
        save_credential method saves credential object into credential_list
        '''
        Credentials.credential_list.append(self)  