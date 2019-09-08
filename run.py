#!/usr/bin/env python3.6
# import pyperclip
from UserAcc import UserAcc 
from credentials import Credentials
import sys
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
#########################################you can logg in
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
    print("Hello Welcome to Password Locker App. '\n'Enter your username and password please?")
   
    print("username")
    print("-"*10)
    username=input()
    print('\n')

    print("password")
    print("-"*10)
    password = input()
    print('\n')

    print(f"Hello {username}  {password}. To continue further you have to create a password and confirm it!")
    print('\n')
    print("Create Password")
    print("-"*20)
    cr_pw = input()

    print("Confirm Password")
    print("-"*20)
    confirm_pswd = input()
    login_users(create_account(username,password,confirm_pswd))
    if cr_pw == confirm_pswd:
        print(f"account for {username}  {password}  successfully created ")
        print('\n')
    else:
        print(f"password {cr_pw} or {conf_pw} Incorrect.Please confirm the password correctly.")
        sys.exit()
       
    print("Use these short codes: lgn - login "," ex - exit the app")
            
    short_code=input().lower()
    if short_code == 'lgn':

        print("now let proceed to login to our account")
        print('\n')
        print('*'*25)
        print("enter your username(the name must be the same us the one you entered previously):")
        print('*'*25)
        login_name=input()
        print('\n')
        print("enter your password")
        print('*'*25)
        passw=input()
        if confirm_pswd == passw and username == login_name:

            print("you are successfully logged in")
            print('\n')
        else:
            print(f"password:{passw} or username{login_name} incorrect. please confirm your password correctly.") 
    elif short_code == 'ex':

        print("Have a nice day! Good Byee....")
        sys.exit()  



        
       
        
       
            
            

if __name__ == '__main__':
    main()
