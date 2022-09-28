import RPi.GPIO as GPIO
import time
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac= [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

n = 0
try:
    while True:
        T = int(input())
        while n != 255:
            GPIO.output(dac, decimal2binary(n))
            time.sleep(T / 512)
            n += 1
        while n != 0:
            GPIO.output(dac, decimal2binary(n))
            time.sleep(T / 512)
            n-=1
        
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()