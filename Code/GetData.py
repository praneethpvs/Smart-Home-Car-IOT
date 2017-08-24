from Location import getLocation
from gps import getMobileLocation
from time import sleep
from RPS import getRPM
from AirFlow import getAirflow

def getData():
    #longitude = getLocation(longitude)
    longitude = getMobileLocation()
    rpm = getRPM()
    if rpm < 100:
        rpm = "normal RPM"
    else:
        rpm = "abnormal RPM"
    airflow = getAirflow()
    message = str(longitude) + "::" + rpm + "::" + "Airflow:"+ str(airflow)
    return message
    # print" see all infor"
    # print longitude
    # print rpm
    # print airflow
    # print "*********"
    # print "final message is" + message
    # print "*********"







