import sqlite3 
import json
import os
import subprocess
import sys
import time
myConnection = sqlite3.connect('NasaAPI.db')
myCursor = myConnection.cursor()
#with open(./cache/)

pichash = subprocess.Popen(['powershell.exe', 'onelinescripts/gethashscript.ps1'],stderr= subprocess.STDOUT,shell=True)
time.sleep(5)
with open ('./cache/hash.txt', "r",encoding="UTF-16") as megahash:
    finalhash = str(megahash.readlines())
    print (finalhash)
    megahash.close
    


with open ('cache/pic.json', "r",encoding="UTF-16") as f:
    hell = (f.readline())
    death= json.dumps(hell,default=False)

    no= json.loads(hell)
    print (type(no))
    print (no["media_type"])
   # print 
    size= os.path.getsize("pictures/pic.jpg")
    
    addPicQuery = """INSERT INTO picture_info (Title,media_type,size,Datedownloaded,Hash)VALUES(?,?,?,?,?);"""
    pic_data=(no["title"],no["media_type"],size,no["date"],finalhash)
    myCursor.execute(addPicQuery, pic_data)
    myConnection.commit()
    myConnection.close
    