import time

def blink(pin):
    pin.value(1)
    print("The LED is on... \n")
    time.sleep(1)
    pin.value(0)
    print("The LED is off.... \n")
    time.sleep(1)