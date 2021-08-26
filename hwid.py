import subprocess
import requests
import time
import os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('insert raw pastebin url here')

try:
    if hwid in r.text:
        pass
    else:
        print('\nHWID is NOT in the database!\n')
        print(f'Your HWID: {hwid}') 
        time.sleep(5)
        os._exit()
except:
    print('\nCould not connect to the database! Exiting program ...')
    time.sleep(5) 
    os._exit() 
   
#if hwid is in database, keep going
os.system('title test)

print('Welcome')
input()
