# Setup code
import network
import time
import machine
import ssd1306
import dht
from umqtt.simple import MQTTClient
import gc

# Configure peripherals
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)
d = dht.DHT22(machine.Pin(0))

# Blink a few times to hint initialization
count = 0
while count < 3:
    oled.fill(1)
    oled.show()
    time.sleep(0.2)
    oled.fill(0)
    oled.show()
    time.sleep(0.2)
    count += 1

# Configure networking
oled.text('net', 0, 10)
oled.show()
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('DEUS','ktm3250a')
while not sta_if.isconnected():
    machine.idle()
oled.text('net ✓', 0, 10)
oled.show()

# Configure Adafruit IO connectivity
oled.text('ada', 0, 20)
oled.show()
myMqttClient = "w1mp-mqtt-client"  # can be anything unique
adafruitIoUrl = "io.adafruit.com"
adafruitUsername = "deanman"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "3ce6af02f16a4d99b64174580db1f11a"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.connect()
oled.text('ada ✓', 0, 20)
oled.show()


while True:
    # Loop code
    d.measure()
    oled.fill(0)
    temp = str(d.temperature())
    hum = str(d.humidity())
    heap = str(gc.mem_free())
    oled.text('t:{}C'.format(temp), 0, 0)
    oled.text('h:{}%'.format(hum), 0, 10)
    oled.text('m:{}'.format(heap), 0, 20)
    oled.show()
    c.publish("deanman/feeds/temperature", temp)
    c.publish("deanman/feeds/humidity", hum)
    #c.publish("deanman/feeds/heap", heap)
    time.sleep(2)

c.disconnect()
