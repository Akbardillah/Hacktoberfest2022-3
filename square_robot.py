import numpy as np
import matplotlib.pyplot as plt

def getJacobian(th):
    J1 = np.matrix([[np.cos(th), 0.], [np.sin(th), 0.], [0., 1.]])
    J2 = np.matrix([[r/2., r/2.], [r/L, -r/L]])
    return J1*J2

r = 0.05 # satuan dalam meter
L = 0.15 # satuan dalam meter
Ts = 0.1 # satuan dalam detik
rpm = [[3., 3.], [-2.892, 3.], [3., 3.], [-2.892, 3.], [3., 3.], [-2.892, 3.], [3., 3.]] # kecepatan roda kiri dan kanan dalam rpm

x = np.matrix([[0., 0., np.radians(0.)]]).transpose()
#print("Posisi Awal : ", x)

# variable untuk merekam posisi setiap sampling
x_plot = [x[0,0]]
y_plot = [x[1,0]]
th_plot = [x[2,0]]
#print(x_plot)

for i in range(0, 50):
    J = getJacobian(x[2, 0])
    q_dot = np.matrix([[rpm[0][1], rpm[0][0]]]).transpose()
    x_dot = J*q_dot
    #update posisi
    x = x + x_dot*Ts
    x_plot.append(x[0,0]) # menambahkan data pada list
    y_plot.append(x[1,0])
    th_plot.append(x[2,0])

for i in range(0, 8):
    J = getJacobian(x[2, 0])
    q_dot = np.matrix([[rpm[1][1], rpm[1][0]]]).transpose()
    x_dot = J*q_dot
    #update posisi
    x = x + x_dot*Ts
    x_plot.append(x[0,0]) # menambahkan data pada list
    y_plot.append(x[1,0])
    th_plot.append(x[2,0])

for i in range(0, 50):
    J = getJacobian(x[2, 0])
    q_dot = np.matrix([[rpm[2][1], rpm[2][0]]]).transpose()
    x_dot = J*q_dot
    #update posisi
    x = x + x_dot*Ts
    x_plot.append(x[0,0]) # menambahkan data pada list
    y_plot.append(x[1,0])
    th_plot.append(x[2,0])

for i in range(0, 8):
    J = getJacobian(x[2, 0])
    q_dot = np.matrix([[rpm[3][1], rpm[3][0]]]).transpose()
    x_dot = J*q_dot
    #update posisi
    x = x + x_dot*Ts
    x_plot.append(x[0,0]) # menambahkan data pada list
    y_plot.append(x[1,0])
    th_plot.append(x[2,0])

for i in range(0, 50):
    J = getJacobian(x[2, 0])
    q_dot = np.matrix([[rpm[4][1], rpm[4][0]]]).transpose()
    x_dot = J*q_dot
    #update posisi
    x = x + x_dot*Ts
    x_plot.append(x[0,0]) # menambahkan data pada list
    y_plot.append(x[1,0])
    th_plot.append(x[2,0])

for i in range(0, 8):
    J = getJacobian(x[2, 0])
    q_dot = np.matrix([[rpm[5][1], rpm[5][0]]]).transpose()
    x_dot = J*q_dot
    #update posisi
    x = x + x_dot*Ts
    x_plot.append(x[0,0]) # menambahkan data pada list
    y_plot.append(x[1,0])
    th_plot.append(x[2,0])

for i in range(0, 50):
    J = getJacobian(x[2, 0])
    q_dot = np.matrix([[rpm[6][1], rpm[6][0]]]).transpose()
    x_dot = J*q_dot
    #update posisi
    x = x + x_dot*Ts
    x_plot.append(x[0,0]) # menambahkan data pada list
    y_plot.append(x[1,0])
    th_plot.append(x[2,0])

print("Posisi Akhir : ", x)
#print(x_plot)

# visualisasi
plt.figure(0)
plt.plot(x_plot[0], y_plot[0], marker='s', color='b')
for i in range(0, len(x_plot), 8):
    plt.quiver(x_plot[i], y_plot[i], np.cos(th_plot[i]), np.sin(th_plot[i]), scale=0.9, scale_units='xy', angles = 'xy', color="r")
plt.plot(x_plot[-1], y_plot[-1], marker='*', color='k')
plt.grid()
plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 2.5)
plt.show()
