from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random

string.alphanum = 'abcd'

# The ThingSpeak Channel ID.
channelID = "1081891"

# The write API key for the channel.
writeAPIKey = "F3YI98GV8UH1HO6B"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "RpiDemo"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "NDN49194Q9PYYVPN"

tTransport = "websockets"
tPort = 80

#random data 
data =10
# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

while(1):

    clientID = ''

# Create a random clientID.
    for x in range(1,16):
        clientID += random.choice(string.alphanum)


    data=data +random.randint(-3,3)
    # build the payload string.
    payload = "field1=" + str(data) + "&field2=" + str(data+1)


    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
        print (" Published 1 = ",data," 2 = ", data+1," to host: " , mqttHost , " clientID= " , clientID)

    except (KeyboardInterrupt):
        break

    except:
        print ("There was an error while publishing the data.")