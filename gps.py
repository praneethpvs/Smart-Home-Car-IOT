from pyicloud import PyiCloudService
from time import sleep

def getMobileLocation():
    api = PyiCloudService('darshan1191@gmail.com', 'Apple1234#')
    
    while True:
         longitude =api.iphone.location().get('longitude')
         return abs(longitude)

    



