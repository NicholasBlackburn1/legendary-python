
import time
import os

# vars
deaths = 0
total = 0
life = 0
name = 0

# var adds
usersuccess = True or False
userfail = True or False
total = usersuccess + life
deaths = userfail
life = usersuccess - userfail
if usersuccess is True:
    total + 1
    if userfail is True:
        deaths + 1
# intro
    print 'Welcome to the Python Game'
time.sleep(1)
name = input('What is your name?')
time.sleep(1)
print name, ('It is nice to meet you')
os.system('python story.py')
