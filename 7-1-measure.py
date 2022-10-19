import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

#Представление двоичного числа
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def binaryonleds(value, leds):
    GPIO.output(leds, decimal2binary(value))

#Измерение значения на выходе тройка-модуля
def adc(comp, dac):
    value = 0
    v1 = 0
    for i in range(8):
        v1 = value + 2 ** (7 - i)
        if v1 < 256:
            signal = decimal2binary(v1)
           # print(signal)
            GPIO.output(dac, signal)
            time.sleep(0.0007)
            comparatorvalue = GPIO.input(comp)
            if comparatorvalue == 1:
                value = v1
    return value

GPIO.setmode(GPIO.BCM)
dac= [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
values = []
time_start = time.time()
fl = False
try:
    while True:
        a = (adc(comp, dac))
        u = a * 3.3 / 2 ** 8
        values.append(u)
        binaryonleds(a, leds)
        if a > 245 and not fl:
            GPIO.output(troyka, 0)
            fl = True
        if a < 5 and fl:
            break
finally:
    time_end = time.time()
    plt.scatter([i + 1 for i in range(len(values))], values, s = 1)
    plt.ylabel("Напряжение на конденсаторе, вольт")
    plt.xlabel("Номер измерения")
    plt.title("Зависимость напряжения на конденсаторе от номера измерения")
    plt.show()
    with open("data.txt", "w") as f:
        for t in values:
            f.write(str(t))
            f.write("\n")
    with open("settings.txt", "w") as f:
            f.write("средняя частота дискретизации: ")
            f.write(str(len(values) / (time_end-time_start)))
            f.write("\n")
            f.write("шаг квантования АЦП: ")
            f.write( str(3.3 / 256))
    print(time_end-time_start)
    print((time_end-time_start)/len(values))
    print(len(values) / (time_end-time_start))
    print(3.3 / 256)
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()