# Smart-Home-Car-IOT  
This is a Sample application that shows how to control the devices located in your home on Raspberry Pi, with your car automatically based on your settings. There is a Message broker runs in AWS Ec2 (Implemented own IOT platform). There are 2 clients located one on each Raspberry Pi where one Raspberry Pi is attached to the Car (_Acts as a sender_) and another client on Raspberry Pi which is attached to your device located in your home (_Acts as a reciever_).

The input is a continuos set of Gps signals and Car data from _Sender_ which is located in a car. The output is a simple LED which is located _on the reciever_ in your home. The Sender continuously send the following data.  
  * GPS information.
  * RPM information.
  * Air Flow Rate information.
  
All the above information is sent to the cloud IoT system storing the status reports and sending GPS information to the Raspberry Pi which is located in your home.  
The Raspberry Pi which is located in your home turns on/off LED lights when GPS information is close to Your home location.

## Basic Setup of the Raspberry Pi.
We need the WiringPi package to manipulate the Raspberry Pi hardware. WiringPi is a PIN based GPIO access library which is used in Raspberry Pi. Install the WiringPi in the Raspberry Pi OS of the device.
```
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
```
## Setup of the Message Broker on Ec2.
Install the Paho-MQTT on the Ec2 which acts as a message broker.
The Python client can be downloaded and installed from PyPI using the pip tool:
```
pip install paho-mqtt
```
* The project can be installed from the repository as well. 
```
git clone https://github.com/eclipse/paho.mqtt.python.git
cd org.eclipse.paho.mqtt.python.git
python setup.py install
```

### Components in the Car IOT System
![Diagram](https://user-images.githubusercontent.com/31011479/29680465-7cd50212-88b9-11e7-8b3d-917507903f78.png)

## Assumptions.
Since we have only one Raspberry Pi we are gonna simulate the situation. We will assume that the sender and the reciver are installed on one Raspberry Pi. The Values of RPM, Air Flow Rate information are simulated using Daemon processes located on Raspberry Pi. The actual car Gps signals are gathered using the GPS signals of the phone which is located in the car. We will send a status report, such as GPS location and the status of the RPM and Airflow, periodically to cloud platform (Ec2 Message broker). Another Daemon process will collect this report from the Message broker continuously and check the GPS signal status. If your GPS location is close to the home location (Which is preset), LED light on the Raspberry Pi will be turned on. If the status of RPM or Airflow is abnormal, a message will be sent to the owner of the car. 

1. Getting the GPS information of car from mobile.
Assume your home is at (latitude, longitude). You will get the car Gps latitude and longitude using the mobile GPS which is located in your car. If your distance between the two GPS cordinates is less than 0.1 mile, we assume that we are close to home. Then, LED light will be turned on.

2. A demon on Raspberry Pi that generates RPM information. A demon on Raspberry Pi that generates Air Flow Rate information.
For RPM and Air Flow Rate, we decided some range of numbers for normal data an abnormal data. we generated the RPM information from 0~100 for normal RPM. If your RPM is more than 100, you will consider it as an abnormal RPM. 

3. A demon on Raspberry Pi that gathers GPS, RPM, and Air Flow Rate information and sending status reports to cloud platform periodically. This data is published to the Message broker. 

4. A demon on your cloud IoT system storing the status reports and sending GPS information to Raspberry Pi. 

5. A demon on Raspberry Pi subscribes to this message. Based on the proximity of the GPS cordinates of the mobile (_to home_)LED light is turned on/off.

__Accessing Wifi of Phone for the Raspberry Pi:__
* Made changes in the wpa_supplicant.conf file
* Added our hotspot details in the file i.e. ID and password(pin)
* After modifying the wpa_supplicant.conf file, used the find my iphone’s pyicloud API.
* By using this Pyicloud API we got the coordinates of longitude and latitude ie the GPS location.

#### Reference Links Used:
https://pypi.python.org/pypi/pyicloud/0.9.1  
https://www.lifewire.com/location-history-google-maps-iphone-1683392  
http://www.komando.com/apps/2756/find-your-lost-iphone-or-ipad/all  
http://www.ubergizmo.com/how-to/track-ios-device/  
##### Watch the demo video below.
[![Demo Video](https://cdn2.iconfinder.com/data/icons/smart-home-part-2/512/1-128.png)](https://drive.google.com/file/d/0B50ljLorR08iSV82Y2VBdWVUUzg/view?usp=sharing)
