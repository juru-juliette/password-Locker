class userAcc:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list

    def __init__(self,username,password,name,email):

      # docstring removed for simplicity

        self.username = username
        self.password = password
        self.name = name
        self.email = email