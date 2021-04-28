#nasa pic thing
#Description:#  This script conncts the subscripts, and is the only script to manuelly start
## Usage:
#  powershell Mainscript.ps1

#  
## History:
#  Date        Author        Description
# 2021-4-27  Riley johnston    creation
import sqlite3
import time
import subprocess
import os 
from os import path
import json
from pprint import pprint
Path = '.\cache\pic.json'
myConnection = sqlite3.connect('NasaAPI.db')
myCursor = myConnection.cursor()


#delete the temp json, so a new one can be retrieved.
def check_for_JSON():
    if path.exists(Path) == True:
        os.remove(Path)
check_for_JSON()
#create the new json, which will compare the date to the database
create_JSON = subprocess.Popen(['powershell.exe', './getjson.ps1'],stderr= subprocess.STDOUT,shell=True)
time.sleep(5)
with open ('cache/pic.json', "r",encoding="UTF-16") as f:
    unreaddata = (f.readline())
    readdata = json.dumps(unreaddata,default=False)
    OBJ = json.loads(unreaddata)
    oldpic= OBJ["date"] #WHERE Datedownloaded=?;", (x,))
    
    myCursor.execute("SELECT Datedownloaded FROM picture_info WHERE Datedownloaded=?;", (oldpic,))
    
    newpic=(myCursor.fetchall())
    if not newpic:
        newpic2 = 0
        print (newpic2)
    else:
        newpic2 = newpic[-1]
        newpic2= str(newpic2)
        newpic2= newpic2.strip("(),'")
        print (newpic2)
        
    if newpic2 == oldpic:
        print ("this picture has been downloaded already. ./pictures/"+ OBJ['date'])

    else: 
        create_pic = subprocess.Popen(['powershell.exe', './scriptone.ps1'],stderr= subprocess.STDOUT,shell=True)
        time.sleep(5)
        sort_pic = exec(open('scriptTwo.py').read())
        os.rename("pictures/pic.jpg", "pictures/"+newpic2+".jpg") 
        set_pic = subprocess.Popen(['powershell.exe', './set_pic.ps1'],stderr= subprocess.STDOUT,shell=True)