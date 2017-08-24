import paho.mqtt.client as mqtt
import os
import socket
import ssl
import RPi.GPIO as GPIO
import json
import time
import datetime
from logging.handlers import RotatingFileHandler
from flask import Flask
from datetime import datetime
from flask import Flask, redirect
import paho.mqtt.client as paho
from GetData import getData
from time import sleep

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

longitude=96.7506047049
cloud=0.0


def on_publish(client,userdata,result):
    print("data published \n")
    pass

def on_connect(client, obj, flags, rc):
    client.subscribe("b827eb2f06f7")

def on_message(client, obj, msg):
    print("Received message from client")
    global cloud
    cloud = float(msg.payload)
    print(str(msg.payload))

def on_subscribe(client, userdata,mid, granted_qos):
    print "userdata : " +str(userdata)


mqttc = paho.Client()
awshost = "ec2-54-202-225-155.us-west-2.compute.amazonaws.com"
awsport = 1883
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe

mqttc.loop_start()

while True:
    picontrol=getData()
    print picontrol
    latt = str(picontrol).split("::")
    longitude=latt[0]
    print(latt[0])
    print cloud
    if (latt[0]  >= str(cloud) and cloud!=0.0):
    #if (latt[0]  >= str(96.766098)):
        print "In loop"
        print latt[0]
        print "turning on light"
        GPIO.output(17, True)
        #sleep(1)
        break
    else:
        mqttc.publish("ack", picontrol)
        print "publish message " + picontrol
        sleep(1)

mqttc.loop_forever()
