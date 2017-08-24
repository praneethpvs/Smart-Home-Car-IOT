from time import sleep

class Location:
	x = 20.20
	y = 10.44
	def _init_(self, x, y):
		self.x = x
		self.y = y

def getLocation(ip):
    location = Location()
    while True:
        temp = float(ip)
        location.x = temp+0.1
        return location.x
        # print(location.x)
        # sleep(1)
        # if (location.x >= 21.20):
        #     break

