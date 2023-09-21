import machine
import time
# pin = machine.Pin(2, machine.Pin.OUT)

# a blink sketch for the es
# while True:
#     pin.value(1)
#     print('pin is turning on...\n')
#     time.sleep(1)
#     pin.value(0)
#     print('pin is going off\n\n')
#     time.sleep(1)


### this code can be used to read the internal temperature of the esp32 in fahrenheits
# but T(f) = theta + 

import esp32
import time
temp = esp32.raw_temperature()

while True:
    print(f'The internal temperature in fahrenheit is: {temp}\n')
    print(f'The internal temperature in degrees centigrades is {(temp-32)*(5/9)}\n')
    time.sleep(1)
