from flask import Flask, redirect
import paho.mqtt.client as paho
import smtplib

#app = Flask(_name_)
# def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

# client = None

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def on_connect(client, obj, flags, rc):
    client.subscribe("ack")

def email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("bhanuarora2607@gmail.com", "Application")

    msg = "Hey Something bad has happend! The RPM value has crossed the threshold."
    server.sendmail("bhanuarora2607@gmail.com", "darshan.parikh.cs@gmail.com", msg)
    server.quit()


def on_message(client, obj, msg):
    print("Received message from client")
    print(str(msg.payload))
    rpm=((str(msg.payload)).split('::'))[1]
    print(rpm)
    if(rpm == "abnormal RPM"):
        print("Value of RPM exceeded 100")
        email()


def on_subscribe(client, userdata,mid, granted_qos):
    print "userdata : " +str(userdata)


mqttc = paho.Client()
awshost = "ec2-54-202-225-155.us-west-2.compute.amazonaws.com"
awsport = 1883
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

mqttc.publish("b827eb2f06f7","96.766098")
print "publish message " + str(96.766098)

mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe

mqttc.loop_forever()
