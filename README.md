# ESP8266 notepad

## WEMOS D1 mini pro

### Erasing Flash memory
`esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`
### Flashing MicroPython
`esptool.py --port /dev/tty.SLAB_USBtoUART --baud 115200 write_flash -fm dio -fs 4MB -ff 40m 0x00000 ~/Downloads/esp8266-20170823-v1.9.2.bin`

https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html 

### Getting MicroPython REPL
`picocom /dev/tty.SLAB_USBtoUART -b115200`

### Exiting REPL session
`Ctrl-a Ctrl-x`

### Driving the WEMOS OLED shield

```
import machine
import ssd1306
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)
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