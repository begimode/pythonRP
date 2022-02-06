# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# test_connect.py
import paho.mqtt.client as mqtt

# The callback function. It will be triggered when trying to connect to the MQTT broker
# client is the client instance connected this time
# userdata is users' information, usually empty. If it is needed, you can set it through user_data_set function.
# flags save the dictionary of broker response flag.
# rc is the response code.
# Generally, we only need to pay attention to whether the response code is 0.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()

pixel_pin = board.D21
    client.subscribe("eskrip/practica/modo/rojo")
    client.subscribe("eskrip/practica/modo/verde")
    client.subscribe("eskrip/practica/modo/azul")
    client.subscribe("eskrip/practica/modo/intensidad")

# The number of NeoPixels
num_pixels = 18

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
while True:
 pixels.fill((r.get(), g.get(), b.get()))
 pixels.show()

"""
for x in range(0, 18):
    pixels[x] = (r.get(), g.get(), b.get())
    pixels.show()
    time.sleep(4)
   
"""
