from gpiozero import LED
import paho.mqtt.client as mqtt

led= LED(15)

def on_connect(client, userdata, flags, resultCode, properties):
    print("Connected with result code: " + str(resultCode))
    client.subscribe("tLights")
    
def on_message(client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode("utf-8")
        print("Message received:", topic, payload)
        
        if topic == "tLights":
            tLights(payload)
            
def tLights(payload):
        if payload == "1":
            led.on()
            print("LED on")
        elif payload == "0":
            led.off()
            print("LED off")
    
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
    
client.connect("192.168.1.20", 1883)
    
client.loop_forever()