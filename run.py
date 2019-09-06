#!/usr/bin/env python3.6
import pyperclip
from UserAcc import UserAcc 
from credentials import Credentials
def create_account(username,password,confirm_pswd):
    '''
    Function to create a new Account
    '''
    new_account = UserAcc(username,password,confirm_pswd)
    return new_account
def create_credential(acc_name,userName,pswd):
    '''
    function to create a new credential
    '''
    new_credential=Credentials(acc_name,userName,pswd)
    return new_credential
#########################################
def login_users(user):
    '''
    function to login user 
    '''
    user.login_user()
def save_credentials(credential):
    '''
    function to login user 
    '''
    credential.save_credential()
def del_credentials(credential):
    '''
    function to delete delete credentials
    '''
    credential.delete_credential()
def find_credential(name):
    '''
    function that finds a credential by name and returns the password
    '''
    return Credential.find_by_name(name)  

def display_credentials():
    '''function that returns all saved credentials
    '''
    return Credential.display_credentials()

def check_existing_credentials(name):
    '''
     Function that check if a credential exists with that account name and return a Boolean
    '''
    return Credential.credential_exist(name)
def main():
    print("Hello Welcome to Password Locker App.")
    # user_name = input()
if __name__ == '__main__':

    main()
