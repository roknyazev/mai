import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import central_gfe
import normal_gfe
import anomalous_gfe

from dpintegrator import DormandPrinceIntegrator


matplotlib.use('Qt5Agg')


longitude_of_the_ascending_node = 300  # OMEGA долгота восходящего узла
inclination = 60  # i наклонение
argument_of_periapsis = -30  # omega аргумент перицентра
semimajor_axis = 11000000  # a
eccentricity = 0.2  # e
initial_true_anomaly = 270  # ipsilon
mu = 398600.436e9


def a_matrix(omega, ipsilon, OMEGA, i):
    u = omega + ipsilon
    elem1 = np.cos(u) * np.cos(OMEGA) - np.sin(u) * np.sin(OMEGA) * np.cos(i)
    elem2 = -np.sin(u) * np.cos(OMEGA) - np.cos(u) * np.sin(OMEGA) * np.cos(i)
    elem3 = np.sin(i) * np.sin(OMEGA)

    elem4 = np.cos(u) * np.sin(OMEGA) + np.sin(u) * np.cos(OMEGA) * np.cos(i)
    elem5 = -np.sin(u) * np.sin(OMEGA) + np.cos(u) * np.cos(OMEGA) * np.cos(i)
    elem6 = -np.sin(i) * np.cos(OMEGA)

    elem7 = np.sin(u) * np.sin(i)
    elem8 = np.cos(u) * np.sin(i)
    elem9 = np.cos(i)
    a = [[elem1, elem2, elem3],
         [elem4, elem5, elem6],
         [elem7, elem8, elem9]]
    return np.array(a)


def transform_into_descart(omega, ipsilon, OMEGA, i, a, e):
    a_m = a_matrix(omega, ipsilon, OMEGA, i)
    p = a * (1 - e ** 2)  # фокальный параметр
    r = np.array([[p / (1 + e * np.cos(ipsilon))],
                  [0],
                  [0]])
    v = np.array([[((mu / p) ** 0.5) * e * np.sin(ipsilon)],
                  [((mu / p) ** 0.5) * (1 + e * np.cos(ipsilon))],
                  [0]])
    return a_m.dot(r), a_m.dot(v)


r_, v_ = transform_into_descart(argument_of_periapsis, initial_true_anomaly, longitude_of_the_ascending_node,
                                inclination,
                                semimajor_axis, eccentricity)

#
#   Центральное ГПЗ
#
model1 = central_gfe.CentralGFE(mu, r_, v_)
integrator1 = DormandPrinceIntegrator(model1, 10, 1e-14, 0, 12000)
SOLUTION1 = []
TIME1 = []
RES_X1 = []
RES_Y1 = []
RES_Z1 = []

#
#   Нормальное ГПЗ
#
model2 = normal_gfe.NormalGFE(mu, r_, v_, semimajor_axis)
integrator2 = DormandPrinceIntegrator(model2, 10, 1e-14, 0, 12000)
SOLUTION2 = []
TIME2 = []
RES_X2 = []
RES_Y2 = []
RES_Z2 = []

#
#   Аномальное ГПЗ
#
model3 = anomalous_gfe.AnomalousGFE(mu, r_, v_, semimajor_axis)
integrator3 = DormandPrinceIntegrator(model3, 10, 1e-14, 0, 12000)
SOLUTION3 = []
TIME3 = []
RES_X3 = []
RES_Y3 = []
RES_Z3 = []


RES_X0 = []
RES_Y0 = []
RES_Z0 = []


for time, solution in integrator1:
    if time is not None:
        for res in solution:
            SOLUTION1.append(res)
        for t in time:
            print("центральное поле: " + str(round(t)))
            TIME1.append(t)

for time, solution in integrator2:
    if time is not None:
        for res in solution:
            SOLUTION2.append(res)
        for t in time:
            print("нормальное поле: " + str(round(t)))
            TIME2.append(t)

for time, solution in integrator3:
    if time is not None:
        for res in solution:
            SOLUTION3.append(res)
        for t in time:
            print("аномальное поле: " + str(round(t)))
            TIME3.append(t)

earth_r = 6400e3
longitude = 0
latitude = 0

JD = 2458849.5
J2k = 2451544.5
d = int(JD - J2k)
t_ = d / 36525
s0g = 24110.54841 + 8640184.812866 * t_ + 0.093104 * (t_ ** 2) - 6.2 * 1e-6 * (t_ ** 3)
s0g_rad = 2 * np.pi * (s0g % 86400) / 86400


def fr(sidereal_time, lat):
    return np.array([[earth_r * np.cos(longitude + sidereal_time) * np.cos(lat)],
                     [earth_r * np.sin(longitude + sidereal_time) * np.cos(lat)],
                     [earth_r * np.sin(lat)]])


for i in range(len(TIME1)):
    time = TIME1[i]
    s = s0g_rad + 7.292115e-5 * (time * 10) + longitude
    r0 = fr(s, 0 * np.pi / 180)
    RES_X0.append(r0[0][0])
    RES_Y0.append(r0[1][0])
    RES_Z0.append(r0[2][0])

for i in range(len(TIME1)):
    solution = SOLUTION1[i][:3]
    RES_X1.append(solution[0])
    RES_Y1.append(solution[1])
    RES_Z1.append(solution[2])


MAGNITUDE1 = []
for i in range(len(TIME2)):
    solution = SOLUTION2[i][:3]
    RES_X2.append(solution[0])
    RES_Y2.append(solution[1])
    RES_Z2.append(solution[2])
    MAGNITUDE1.append((solution[0]**2 + solution[1]**2 + solution[2]**2)**0.5)


MAGNITUDE2 = []
for i in range(len(TIME3)):
    solution = SOLUTION3[i][:3]
    RES_X3.append(solution[0])
    RES_Y3.append(solution[1])
    RES_Z3.append(solution[2])
    MAGNITUDE2.append((solution[0] ** 2 + solution[1] ** 2 + solution[2] ** 2) ** 0.5)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(RES_X0, RES_Y0, RES_Z0)
ax.plot(RES_X1, RES_Y1, RES_Z1)
ax.plot(RES_X2, RES_Y2, RES_Z2)
ax.plot(RES_X3, RES_Y3, RES_Z3)

plt.show()
