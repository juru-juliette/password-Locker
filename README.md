# password-Locker
this application will help us manage our passwords and even generate new passwords for us.

## Description
The password locker is an app that help the user generate and store passwords that he/she uses regulary. The user can either create password or generate it. The user can also delete a password of his choice all display them but first he/she has to log into the app.
## Installation Requirements
* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Run python3.6 run.py code in the terminal to launch.

For now the project is only viewable in the terminal!

## App Specifications
### The following is what my App should handle:

#### Example Intput : 
user enters username and password
##### Output:
 To get access you have to log in

#### Example Input : 
user inputs password and confirm it correctly
#####  Output:
user is now in the app and can start to create or generate password

#### Example Input:
user inputs password and confirms it wrongly
##### Output
user exit the app immediately

#### Example Input:
user chooses any short code, example: cp
##### Output
the user is directed to do what the short code executes, example:cp -create password

#### Other behaviors(short codes):
* cp : create a new password
* dp : display created password
* fp : find a password
* delp : to delete password
* gp : generate password
* ex : exit app

### Bugs
Since there is no database to support the app, once you exit or log out of a session you loose all the credentials and created user. You have to create a new user for every session. You can still use the default login but if you exit the app, you will still loose all the credentials you created.
## Technologies Used
* Python
* Git-Hub
* Terminal
## Support and contact details
E-mail:kangabejuliette@gmail.com
Phone:0787873242-0789557608.
### License
**[MIT](http://choosealisence.com/licenses/mit/)**
Copyright (c) 2019 **KANGABE JULIETTE**