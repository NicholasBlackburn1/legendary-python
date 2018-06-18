
import time
import os

# vars
deaths = 0
total = 0
life = 0
usersuccess = True or False
userfail = True or False
total = usersuccess + life
deaths = userfail
life = usersuccess - userfail

# intro
print 'Welcome to the Python Game',
time.sleep(1)
print 'You are a hacker and you want to hack in to the government\n'
time.sleep(1)
# slection menu
print ('''You need to infect one of the FBI computers\n

      here are your available actions:\n

     1. Stay at home and send fishing emails to FBI employies\n
     2. Go to Starbucks and exploit the FBI's unupdated file server\n
     3. Go to the local gang hideout and get them help\n
     4. Walk into the FBI headquartors and threaten the receptionist with Ak\n
     5. Stay Home with your Neko companion and Snuggle together\n
     ''')
menu_number_text = input('Enter the number you want\n')
menu_number = int(menu_number_text)
# menu number 1
if menu_number == 1:
    print('You are sending fishing attacks to the FBI')
    time.sleep(2)
    os.system('python video.py')
    print('then you get a surprise')
#  menu number 2
if menu_number == 2:
    print ('you are at Starbucks now exploiting the FBIs File server')
