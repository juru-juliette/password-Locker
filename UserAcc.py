class UserAcc:
    """
    Class that generates new instances of user.
    """

    user_list = [] # Empty user list

    def __init__(self,Username,Password):

      # docstring removed for simplicity

        self.Username = Username
        self.Password = Password
    def save_user(self):

        '''
        save_user method saves users objects into user_list
        '''

        UserAcc.user_list.append(self)