import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

#чтение данных
data = np.loadtxt("data.txt", delimiter='\n')
frequency, quant_step = np.loadtxt("settings.txt", delimiter='\n')
time = np.array([i * 1 / frequency for i in range(data.size)])

fig, ax = plt.subplots(figsize=(16, 10), dpi=500)

ax.plot(time, data, lw = 1, c = "b", marker = "o", ms = 5, markerfacecolor = "violet", markevery = 300, label = "V(t)")
#настройка легенды
ax.legend(fontsize=10)

#настройка сетки
ax.axis([time.min(), time.max()+1, data.min(), data.max()+0.2])
ax.minorticks_on()
ax.tick_params(axis = 'both', which = 'major', labelsize = 8, labelrotation = 45)
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.grid(which='major', linestyle='-', linewidth=0.1, color = "grey")
ax.grid(which='minor', linestyle = ':', color = "green", linewidth = 0.1)

#настройка текста
index = data.argmax()
ax.text(6 * 10, 0.5, 'Время зарядки ' + str(time[index])[:4] + "c", fontsize = 10)
ax.text(6 * 10, 0.7, 'Время разрядки ' + str(time[-1]-time[index])[:4] + "c", fontsize = 10)

#настройка подписей осей и названия графика
plt.xlabel('Напряжение, вольт', fontsize=10, bbox = {'pad': 0.1,'facecolor': 'white','edgecolor': 'white'})
plt.ylabel('Время, секунда', fontsize=10, bbox = { 'pad': 0.1,'facecolor': 'white','edgecolor': 'white'})
ax.set_title('Процесс заряда и разряда конденсатора', fontsize=15)
fig.savefig('graph.svg')
fig.savefig('graph.png')
#plt.show()