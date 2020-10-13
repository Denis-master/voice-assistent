import paho.mqtt.client as paho
import datetime #as datetime
print("--------------------------")
print("(c) Denis Petrov 2020 v1.0")
print("--------------------------")
ipa="192.168.2.190"
tpk = "meteo2"
#datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
def on_subscribe(client, userdata, mid, granted_qos):
    return

def on_message(client, userdata, msg):
    fame = datetime.date.today()
    
    fal = open("/home/pi/"+str(fame) + ".txt","a")
    #print(fame)
    
        
    now = datetime.datetime.now()
    print("-----"+str(now)+"-----")
    print("--------------------")
    print("topic "+ str(msg.topic))
    print(float(msg.payload))
    print("--------------------")
    print('\n')

    fal.write(str(float(msg.payload))+ '\n')

    #fal.write('\n')
    fal.close()
client = paho.Client()
client.username_pw_set("mqttusr", "mqttpass")
client.connect(ipa, 1883)
client.on_subscribe = on_subscribe
client.on_message = on_message

client.subscribe(tpk + "/temperature", qos=1)
client.subscribe(tpk+"/humidity", qos=1)
client.subscribe(tpk+"/pressure", qos=1)

client.loop_forever()

