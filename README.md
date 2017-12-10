# MicroPython
## Erasing Flash memory

```
# Wemos D1 R2
esptool.py --port /dev/tty.wchusbserial14230  erase_flash

# Wemos D1 mini Pro
esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
```

## Flashing MicroPython

```
# Wemos D1 mini Pro
esptool.py --baud 115200 --port /dev/tty.SLAB_USBtoUART write_flash -fm dio -fs 4MB -ff 40m 0x00000 ~/Downloads/esp8266-20171101-v1.9.3.bin

# Wemos D1 R2
esptool.py --port /dev/tty.wchusbserial14230 --baud 115200 write_flash --flash_size=detect 0 ~/Downloads/esp8266-20171101-v1.9.3.bin

# eBoxmaker ESP32
esptool.py --port /dev/tty.SLAB_USBtoUART --baud 115200 write_flash --flash_size=detect 0x1000 ~/Downloads/esp32-20171126-v1.9.2-443-g236297f4.bin
```

https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html

## MicroPython REPL

```
# Getting into the REPL
picocom /dev/tty.SLAB_USBtoUART -b115200
# Exiting REPL when using picocom
`Ctrl-a Ctrl-x`

# or
screen /dev/tty.SLAB_USBtoUART 115200
# Exiting REPL when using screen
`Ctrl-a k`

```

## Driving SSD1306 OLED peripheral


```
import machine, ssd1306

# D1 mini Pro
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

# Wemos OLED shield
oled = ssd1306.SSD1306_I2C(64, 48, i2c)

# Generic 128 x 64 OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(1)
oled.show()
oled.fill(0)
oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()
```

https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display/micropython

### Driving the DHT22 temperature/humidity sensor

```
import dht
import machine

d = dht.DHT22(machine.Pin(5)) # corresponds to D1
d.measure()
d.temperature() # eg. 23.6 (°C)
d.humidity()    # eg. 41.3 (% RH)
```

### OLED + temperature

```
while True:
	time.sleep(2);
	d.measure();
	oled.fill()
	oled.text(str(d.temperature()), 0, 0)
	oled.show()
```
