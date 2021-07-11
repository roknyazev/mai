import dpintegrator
import kepler_model

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')

model = kepler_model.KeplerEphemerisModel()

minute = 60
hour = 60 * minute
day = 24 * hour
fTIME = day * 365
OMEGA = 7.292115e-5

JD = model.JD
J2k = 2451544.5
d = int(JD - J2k)
t_ = d / 36525
s0g = 24110.54841 + 8640184.812866 * t_ + 0.093104*(t_**2) - 6.2*1e-6*(t_**3)
s0g_rad = 2 * np.pi * (s0g % 86400) / 86400

#latitude = 54.66 * np.pi / 180  # широта
#longitude = 20.5 * np.pi / 180  # долгота

latitude = 90 * np.pi / 180
longitude = 0 * np.pi / 180

gnomon_len = 1
earth_r = 6371300


def fr(sidereal_time):
    return np.array([[earth_r * np.cos(longitude + sidereal_time) * np.cos(latitude)],
                     [earth_r * np.sin(longitude + sidereal_time) * np.cos(latitude)],
                     [earth_r * np.sin(latitude)]])


TIME = []
RES_X = []
RES_Y = []
RES_Z = []

RES_X2 = []
RES_Y2 = []
RES_Z2 = []

MAGNITUDE = []

SOLUTION = []
integrator = dpintegrator.DormandPrinceIntegrator(model, 60, 1e-16, 0, fTIME)
for time, solution in integrator:
    if time is not None:
        for res in solution:
            SOLUTION.append(res)
        for t in time:
            TIME.append(t)

flag = 1
init_time = 0
duration = 0
Dur = []
day = 0
Days = []
t8 = []
t20 = []

for i in range(len(TIME)):
    time = TIME[i]
    solution = SOLUTION[i]

    re = -np.array([solution[:3]]) * 1000
    re0 = re/np.linalg.norm(re)  # Нормированный вектор луча солнца
    s = s0g_rad + OMEGA * time + longitude  # Звездное время места земли (рад)

    r = fr(s)
    r0 = r/np.linalg.norm(r)  # Нормированный радиус-вектор расположения точки гномона
    re_ = (-gnomon_len / np.dot(re0, r0)) * re0

    rg = gnomon_len*r0
    rsh = rg + re_.T
    RES_X.append(re[0][0] / 1000)
    RES_Y.append(re[0][1] / 1000)
    RES_Z.append(re[0][2] / 1000)

    angle = np.arccos(np.dot(re, r) / ((np.linalg.norm(re)) * (np.linalg.norm(r))))

    if angle < (np.pi / 2 - 0.1):
        if init_time == 0:
            init_time = time / 60
        flag = 0
        duration += 1
        MAGNITUDE.append(np.linalg.norm(rsh))
        RES_X2.append(rsh[0][0])
        RES_Y2.append(rsh[1][0])
        RES_Z2.append(rsh[2][0])
    else:
        if flag == 0:
            Dur.append(duration)
            day += 1
            Days.append(day)
            t8.append(480)
            t20.append(1200)
            duration = 0
        flag = 1
        MAGNITUDE.append(0)

#plt.plot(Days, t8)
#plt.plot(Days, t20)
#plt.plot(Days, Dur)
plt.plot(TIME, MAGNITUDE)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot(RES_X, RES_Y, RES_Z)
ax.plot(RES_X2, RES_Y2, RES_Z2)

plt.show()
