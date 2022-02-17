import win32gui
import os
from fuzzywuzzy import fuzz
import pyperclip
import string    
import random
from pynput.keyboard import Listener
import win32gui
from fuzzywuzzy import fuzz
import threading

def closewindow():
    w=win32gui
    x=w.GetWindowText(w.GetForegroundWindow())
    print(x)
    if x[-len("Google Chrome"):]=='Google Chrome':
        os.system("TASKKILL /F /IM chrome.exe")
    if x[-len("Discord"):]=='Discord':
        os.system("TASKKILL /F /IM Discord.exe")
    if x[-len("WhatsApp"):]=='WhatsApp':
        os.system("TASKKILL /F /IM WhatsApp.exe")
    if x[-len("Telegram"):]=='Telegram':
        os.system("TASKKILL /F /IM Telegram.exe")
    if x[-len("Microsoft Teams"):]=='Microsoft Teams':
        os.system("TASKKILL /F /IM Teams.exe")
    if x[-len("Edge"):]=='Edge':
        os.system("TASKKILL /F /IM msedge.exe")
    if x[-len("Mozilla Firefox"):]=="Mozilla Firefox":
        os.system("TASKKILL /F /IM firefox.exe")

def iterate(word):
    with open("1-1000.txt") as f:
        flag=0
        for line in f:
            if fuzz.ratio(word,line)>=75:
                flag=1
        return flag

def copypaste():
    pyperclip.copy(str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 25))))#impulse
    while(1):
        text = pyperclip.waitForNewPaste()
        text1= pyperclip.paste()
        print(text1)
        if iterate(text1)==1:
            closewindow()
            pyperclip.copy(str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 25))))

lis=[]

def log_keystroke(key):
    key=str(key).replace("'","")
    global lis
    if key=="Key.space":
        key=" "
        lis.append(" ")
    if key=="Key.enter":
        print(lis)
        key=""
        s=""
        for i in lis:
            s=s+i
        if(iterate(s)==1):
            closewindow()
        lis=[]
    if key=="Key.shift_r" or key=="Key.shift" or key=="Key.ctrl_l" or key=="Key.ctrl_r":
        key=""
        lis.append(key)
    if key=="Key.backspace":
        if lis!=[]:
            lis.pop()
    if len(key)==1:
        lis.append(key)

def keylog():
    with Listener(on_press=log_keystroke) as l:
        l.join()

def websearchclose():
    while(1):
        w=win32gui
        x=w.GetWindowText (w.GetForegroundWindow())
        with open("1-1000.txt") as f:
            flag=0
            for line in f:
                if fuzz.ratio(x[:len(line)],line)>=75:
                    closewindow()

thread1 = threading.Thread(target=copypaste)
thread2 = threading.Thread(target=websearchclose)
thread3 = threading.Thread(target=keylog)
thread1.start()
thread2.start()
thread3.start()