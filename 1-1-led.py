import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)
for i in range(10000000):
    GPIO.output(14, GPIO.input(15))
