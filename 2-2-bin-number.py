import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time
GPIO.setmode(GPIO.BCM)
dac= [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 1, 1, 1, 1, 1, 1, 1]
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()

#u = [3.259, 1.628, 0.820, 0.502, 0.487, 0.487]
#number = [255, 127, 64, 32, 5, 0]
#plt.plot(number, u)
#plt.show()