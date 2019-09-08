class UserAcc:
    """
    Class that generates new instances of user.
    """

    user_list = [] # Empty user list

    def __init__(self,Username,Password,confirm_pswd):

      # docstring removed for simplicity

        self.Username = Username
        self.Password = Password
        self.confirm_pswd = confirm_pswd
    def save_user(self):

        '''
        save_user method saves users objects into user_list
        '''

        UserAcc.user_list.append(self)
    # def login_user(self)
    #     '''
    #     login_user method save users into users list object
    #     '''
    #     UserAcc.user_list.append(self)
