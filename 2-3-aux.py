import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
for i in range(1000000):
    for j in range(len(aux)):
     GPIO.output(leds[j], GPIO.input(aux[j]))
GPIO.output(leds, 0)
GPIO.cleanup()