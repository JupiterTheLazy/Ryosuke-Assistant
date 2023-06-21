import webbrowser
import time
import os
import playsound

print('Ryōsuke: Hello, Master')
from playsound import playsound
playsound('C:\\Users\\Jupter\\Documents\\speak\\Hi master.mp3')
while True:
    print('Ryōsuke: How can I help you?')
    action=input('You: ')

    if action=="gm":
        print('Ryōsuke: Good Morning!')
        playsound('C:\\Users\\Jupter\\Documents\\speak\\good-morning.mp3')
        time.sleep(1)
        notion = "https://www.notion.so/"               
        webbrowser.open(notion)
    elif action=="study":
        print('Ryōsuke: Preparing study place...')
        time.sleep(1)
        stud = "https://pomofocus.io/app"
        webbrowser.open(stud)
        radio = "https://radio.garden/listen/ashiyaradio/agGPOrdP"
        webbrowser.open(radio)         
    elif action=="music":
        print('Ryōsuke: Preparing music...')
        time.sleep(1)
        music = "https://youtube.com/playlist?list=PLw4wL1eg6DUxqobY8-9r16ZYg4Dng6I0O"
        webbrowser.open(music)        
    elif action=="bye":
        print('Ryōsuke: See you later.')
        playsound('C:\\Users\\Jupter\\Documents\\speak\\see you later.mp3')
        #time.sleep(1)
        break
    else:
        print('Ryōsuke: Invalid input, plase try again')
