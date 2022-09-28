import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac= [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
u = 0
try:
    while True:
        n = (input())
        if n == 'q':
            raise (KeyError)
        n = float(n)
        if float(n) < 0 or int(n) != float(n) or float(n) > 255:
            raise TypeError()
        n = int(n)
        GPIO.output(dac, decimal2binary(n))
        u = 3.3 / 2 ** 8 * n
        print(u , " Вольт")

except ValueError:
    print("Введите число")
except TypeError:
    print("Введите целое положительное число от 0 до 255")
except KeyError:
    print("Ввод значений завершён")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
