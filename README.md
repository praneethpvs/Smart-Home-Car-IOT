# Smart-Home-Car-IOT  
This is a Sample application that shows how to control the devices located in your home on Raspberry Pi, from your car. There is a Message broker runs in AWS Ec2 (Implemented own IOT platform). There are 2 clients located one on each Raspberry Pi where one Raspberry Pi is attached to the Car (_Acts as a sender_) and another client on Raspberry Pi which is attached to your device located in your home (_Acts as a reciever_).

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

### ![Diagram Explaining the Components in the Car IOT System](/home/pvs/Pictures/Car-IOT.png)

