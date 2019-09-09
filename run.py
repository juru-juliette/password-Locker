#!/usr/bin/env python3.6
# import pyperclip
from UserAcc import UserAcc 
from credentials import Credentials
import sys
## user
def create_account(username,password,confirm_pswd):
    '''
    Function to create a new Account
    '''
    new_account = UserAcc(username,password,confirm_pswd)
    return new_account
def login_users(user):
    '''
    function to login user 
    '''
    user.login_user()
## credential
def create_credential(account_name,userName,password):
    '''
    function to create a new credential
    '''
    new_credential=Credentials(account_name,userName,password)
    return new_credential


def save_credential(credential):
    '''
    function to login user 
    '''
    Credentials.save_credential()
def display_credentials():
    '''
    function that returns all saved credentials
    '''
    return Credentials.display_credentials()
def find_credential(name):
    '''
    function that finds a credential by name and returns the password
    '''
    return Credentials.find_by_name(name)
def check_existing_credentials(name):
    '''
     Function that check if a credential exists with that account name and return a Boolean
    '''
    return Credentials.credential_exist(name)  
def del_credentials(credential):
    '''
    function to delete delete credentials
    '''
    Credentials.delete_credential()

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

    print(f"Hello {username}  {password}. To continue further you have to confirm your password!")
    print('\n')
    print("Confirm Password")
    print("-"*20)
    confirm_pswd = input()
    login_users(create_account(username,password,confirm_pswd))
    if password == confirm_pswd:
        print(f"account for {username}  {password}  successfully created ")
        print('\n')
    else:
        print(f"password {conf_pw} Incorrect.Please confirm the password correctly.")
        sys.exit()
       
    print("Use these short codes: lgn - login "," ex - exit the app")
            
    short_code=input().lower()
    if short_code == 'lgn':

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
#########################################you can logg in
        else:
            print(f"password:{passw} or username{login_name} incorrect. please confirm your password correctly.") 
    elif short_code == 'ex':

        print("Have a nice day! Good Byee....")
        sys.exit() 
#############################credentials###############################
    while True :
        print("Use these short codes:cp - create a new password"," dp - display created password ", " fp - find a password", "delp - to delete password", "gp - generate password"," ex - exit app")
        short_code = input().lower()
        if short_code == 'cp':
            print("New Password")
            print('*'*10)
            print("Account name")
            print('-'*10)
            account_name = input()
            print("username")
            print('-'*10)
            userName = input()
            print("password")
            print('-'*10)
            password = input()
            save_credential (create_credential(account_name,userName,password)) 
            print('\n')
            print(f"new password for this account {account_name} \n username: {userName} \n password :{password} is created") 
            print('\n')
        elif short_code == 'ex':
            print("Have a nice day! Good Byee....")
            sys.exit() 
        elif short_code == 'dp':
            if display_credentials():
                print("this is a list of all your password")
                print('\n')

                for credentials in display_credentials():
                   
                    print (f"{credentials.account_name} {credentials.userName} {credentials.password}")
                    print('\n')
            else: 
                print('\n')
                print("you dont have any password saved yet")
                print('\n')
        # elif short_code == 'fp':
        #     print("Enter the name of the account you want to search password for:")
        #     search_name = input()
        #     if check_existing_credentials(search_name):
        #         search_name = find_credential(search_name)
        #         print(f"account name....{search_name.account_name} password {search_name.password}")
        #         print('-'*20)
        #         print("account name does not exist")
        # elif short_code == "delp":
        #     print("Enter the name of you want to delete")
        #     search_name = input()
        #     if check_existing_credentials(search_name):
        #         Credential = find_credential(search_name)
        #         del_credentials(Credential)
        #         print(f"{credential.account_name} deleted")
        #         print('\n')
        #         print ("credential and password deleted")
        #     else:
        #         print("Account you want to delete doesn't exist")



              




        
       
        
       
            
            

if __name__ == '__main__':
    main()
