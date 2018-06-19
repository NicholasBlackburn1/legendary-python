
import time
import os
import playsound
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
print 'Welcome to the Python Game\n',
time.sleep(1)
print('Today is Dec 15 2018')
time.sleep(1)
print 'You are a hacker and you want to hack in to the government\n'
time.sleep(1)
# slection menu
print ('''You need to infect one of the FBI computers\n

      here are your available actions:\n

     1. Stay at home and send fishing emails to FBI employies\n
     2. Go to Starbucks and exploit the FBI's unupdated file server\n
     3. Walk into the FBI headquartors and threaten the receptionist with Ak\n
     4. Stay Home with your Neko companion and Snuggle together by the fireplace\n
     ''')
menu_number_text = input('Enter the number you want\n')
menu_number = int(menu_number_text)
# menu number 1
if menu_number == 1:
    print('You are sending fishing attacks to the FBI')
    time.sleep(2)
    os.system('python video.py')
    time.sleep(2)
    print('then you get a surprise')
    time.sleep(1)
    os.system('python video1.py')
    time.sleep(2)
    print('you got killed by an FBI officer')

#  menu number 2
if menu_number == 2:
    print ('you are at Starbucks now exploiting the FBIs File server')
    time.sleep(2)
    os.system('python video2.py')
    time.sleep(1)
    print ('It actully looks like you are almost there')
    time.sleep(2)
    os.system('python video3.py')
    time.sleep(2)
    print('just 2 more seconds')
    time.sleep(1)
    os.system('python video4.py')
    time.sleep(2)
    print('your computer blew up when your were downloading the information ')


# menu number 3
if menu_number == 3:
    print('You are walking up to the FBI ')
    time.sleep(2)
    os.system('python video5.py')
    time.sleep(2)
    print ('Then you are slowly backing away')
    time.sleep(2)
    print ('you never came back')
    # menu number 4
    if menu_number == 4:
        print ('well your favorite moment')
    time.sleep(2)
    os.system('python video6.py')
    time.sleep(2)
    print ('well this is the bestday ever')
    time.sleep(1)
    os.system('python video7.py')
