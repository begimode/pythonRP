import board
import time
import neopixel
import paho.mqtt.client as mqtt

pixel_pin = board.D21
num_pixels = 16

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness= 0.5, pixel_order = ORDER)

def on_connect(client, userdata, flags, rc):
    print ("Se conecto con mqtt " + str(rc))
    client.subscribe("eskrip/practica/movimiento")
    
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if str(msg.payload) == "b'Esta movimiento'":
        pixels.fill((0,255,0))
        pixels.show()
        time.sleep(1)
    else:
        pixels.fill((0,0,0))
        pixels.show()
        time.sleep(1)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60 )


def wheel(pos):
    
    if pos<0 or pos >255:
        r=g=b=0
        
    elif pos <85:
        r=int(pos*3)
        g =int(255 - pos *3)
        b=0
        
    elif pos<170:
        pos -=85
        r= int (255 - pos *3)
        g=0
        b = int (pos*3)
        
    else:
        pos -=170
        r=0
        g=int (pos *3)
        b = int (255 - pos * 3)
        
    return (r,g,b) if ORDER in (neopixel.RGB , neopixel.GRB) else (r,g,b,0)


def rainbow_cycle(wait):
    for j in range (255):
        for i in range(num_pixels):
            pixel_index = (i*256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        
    
client.loop_forever()
    
            
            
