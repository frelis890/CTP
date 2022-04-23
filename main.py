import matplotlib.pyplot as plt
import numpy as np

# załadowanie i wydruk wykresu
dane = np.loadtxt(r"C:\Users\HP\Desktop\PK\CTP\GL02.csv", unpack=True, delimiter=',', skiprows=1)

time = dane[0]
v0 = dane[1]
v1 = dane[2]
v2 = dane[3]
v3 = dane[4]

plt.plot(time, v0, c = 'red', label = 'Voltage 0')
plt.plot(time, v1, c = 'purple', label = 'Voltage 1')
plt.plot(time, v2, c = 'orange', label = 'Voltage 2')
plt.plot(time, v3, c = 'turquoise', label = 'Voltage 3')

plt.title('Wykres CTP')
plt.xlabel('Time[s]')
plt.ylabel('Voltage')

plt.axhline(0, color='black')  # x = 0
plt.axvline(0, color='black')  # y = 0

plt.legend()
plt.savefig('Wykres1.pdf')
plt.show()

# ponowne drukowanie wykresu ze zbliżeniem
plt.plot(time, v0, c = 'red', label = 'Voltage 0')
plt.plot(time, v1, c = 'purple', label = 'Voltage 1')
plt.plot(time, v2, c = 'orange', label = 'Voltage 2')
plt.plot(time, v3, c = 'turquoise', label = 'Voltage 3')

plt.title('Wykres CTP')
plt.xlabel('Time[s]')
plt.ylabel('Voltage')

plt.axhline(0, color='black')  # x = 0
plt.axvline(0, color='black')  # y = 0

plt.xlim(36.00, 38.00)
plt.ylim(-4.00, 6.00)

plt.legend()
plt.savefig('Wykres1-zblizenie.pdf')
plt.show()