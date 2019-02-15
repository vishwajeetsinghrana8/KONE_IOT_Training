import paho.mqtt.client as mqtt
import ssl

rootca='E:/H Drive/RPI/AWSIOT/iot_thing/AmazonRootCA1.pem.txt'
certificate='E:/H Drive/RPI/AWSIOT/iot_thing/3fefa9c0ce-certificate.pem.crt'
keyfile='E:/H Drive/RPI/AWSIOT/iot_thing/3fefa9c0ce-private.pem.key'
c=mqtt.Client()
c.tls_set(rootca,certfile=certificate,keyfile=keyfile,cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None)

c.connect('a20h7874zb7gto-ats.iot.us-east-2.amazonaws.com',8883)

def onc(c,userdata,flags,rc):
    print("Succesfully connect to Amazon with RC",rc)
    c.subscribe("mytopic/iot")

def onm(c,userdata,msg):
    m=msg.payload.decode()
    print(m)
    if m == "hello":
        c.publish('mytopic/iot','Hello from python to Amazon')

c.on_connect=onc
c.on_message=onm
c.loop_forever()
