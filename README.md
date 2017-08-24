# Smart-Home-Car-IOT  

This is a Sample application that shows how to control the devices located in your home on Raspberry Pi, from your car. There is a Message broker runs in AWS Ec2 (Implemented own IOT platform). There are 2 clients located one on each Raspberry Pi where one Raspberry Pi is attached to the Car (_Acts as a sender_) and another client on Raspberry Pi which is attached to your device located in your home (_Acts as a reciever_).

The input is a continuos set of Gps signals and Car data from _Sender_ which is located in a car. The output is a simple LED which is located _on the reciever_ in your home. The Sender continuously send the following data.
  * GPS information.
  * RPM information.
  * Air Flow Rate information.
  
 the end
