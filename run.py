#!/usr/bin/env python3.6
import pyperclip
from UserAcc import UserAcc 
from credentials import Credentials
def create_account(Username,Password,confirm_pswd):
    '''
    Function to create a new Account
    '''
    new_account = UserAcc(Username,Password,confirm_pswd)
    return new_account
def create_credential(acc_name,password):
    '''
    function to create a new credential
    '''
    new_credential=Credentials(acc_name,userName,password)
    return new_credential
