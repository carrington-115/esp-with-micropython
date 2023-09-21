import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)

# a blink sketch for the es
while True:
    pin.value(1)
    print('pin is turning on...\n')
    time.sleep(1)
    pin.value(0)
    print('pin is going off\n\n')
    time.sleep(1)