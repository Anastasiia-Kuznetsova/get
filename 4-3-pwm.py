import RPi.GPIO as GPIO
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 1000)
pwm.start(0)

dac= [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
#GPIO.output(dac, [1,1,1,1,1,1,1,1])
try:
    while True:
        dc = int(input())
        pwm.ChangeDutyCycle(dc) 
        print(3.3 * dc / 100)
finally:
    GPIO.output(led, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()