# subscriber.py
import paho.mqtt.client as mqtt
import board
import time
import neopixel

pixel_pin = board.D21
num_pixels = 20

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness= 1, pixel_order = ORDER)

def on_connect(client, userdata, flags, rc):
    print("Se conecto con mqtt" + str(rc))
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe("eskrip/practica/status/apagar")
    client.subscribe("eskrip/practica/status/encender")
   
    client.subscribe("eskrip/practica/color/rojo")
    client.subscribe("eskrip/practica/color/verde")
    client.subscribe("eskrip/practica/color/azul")
    client.subscribe("eskrip/practica/color/intensidad")
   


# the callback function, it will be triggered when receiving messages

def on_message(client, userdata, msg):
    
    #re,gr,bl = 255, 255, 255
    #encendido = True
    inte = 100
    
    print(f"{msg.topic}{msg.payload}")
  
    "time.sleep(1)"
    
    
    if str (msg.payload)=="b'Encender'":
        global encendido
        encendido = True
        pixels.fill((255,255,255))
        pixels.show()
    elif str (msg.payload)=="b'Apagar'":
        encendido = False
        pixels.fill((0,0,0))
        pixels.show()
        
          
    if (msg.topic == "eskrip/practica/color/rojo") and (encendido == True):
        red=str(msg.payload, 'utf-8')
        print(red)
        global re
        re = int(red)
                    #on_color(re,0,0)
                    
    elif (msg.topic == "eskrip/practica/color/verde") and (encendido == True):
         green=str(msg.payload, 'utf-8')
         print(green)
         global gr
         gr = int(green)

                    
    elif (msg.topic == "eskrip/practica/color/azul") and (encendido == True):
         blue=str(msg.payload, 'utf-8')
         print(blue)
         global bl
         bl = int(blue)
         on_color(re,gr,bl)
         
                        
         
    elif (msg.topic == "eskrip/practica/color/intensidad") and (encendido == True):
         intensidad=str(msg.payload, 'utf-8')
         print(intensidad)
         inte = int(intensidad)
         pixels.brightness = (inte/100)
      
    
    
    
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect("broker.hivemq.com", 1883, 60)

def on_color(ree,grr,bll):
    
    pixels.fill((ree, grr, bll))
    pixels.show()
    
    




# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()

