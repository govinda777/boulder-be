import ssl
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

awshost = "a12sdqmvxrmcs4-ats.iot.us-east-1.amazonaws.com"
awsport = 8883

caPath = "./teste.cert.pem" # Root certificate authority, comes from AWS with a long, long name
certPath = "./teste.public.key"
keyPath = "./teste.private.key"

client.tls_set(caPath, 
            certfile=certPath, 
            keyfile=keyPath, 
            cert_reqs=ssl.CERT_REQUIRED, 
            tls_version=ssl.PROTOCOL_TLSv1_2, 
            ciphers=None)

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()