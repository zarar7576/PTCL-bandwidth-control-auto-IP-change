#You can use this simple script to check if you have a valid internet connection it plays a sound when it finds a connecion

from urllib.request import urlopen
from playsound import playsound
import time

def internet_on():
    try:
        response = urlopen('https://www.google.com/',timeout=1)
        return True
    except: 
        return False

connections=1
##print("Connecton retry: "+str(connections),end="\r")


while 1:
    if not(internet_on()):
        connections+=1
        print("Connecton retry: "+str(connections),end="\r")
    else:
        break
    
print("\n")
print(internet_on())


playsound('internetfound.mp3')
print("Internet connection found")

time.sleep(10)

quit()
