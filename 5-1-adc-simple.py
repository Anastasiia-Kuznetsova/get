import RPi.GPIO as GPIO
import time
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc(comp, dac):
    for value in range(256):
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.005)
        comparatorvalue = GPIO.input(comp)
        if comparatorvalue == 0:
            return value

GPIO.setmode(GPIO.BCM)
dac= [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
       a = (adc(comp, dac))
       print("цифровое-", a, "напряжение", end = " ")
       print("{:.3f}".format(a * 3.3 / 2 ** 8))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()