from dpintegrator import AbstractModel
from normal_gfe import *
import mass
import numpy as np


MASS = mass.M
X = mass.X
Y = mass.Y
Z = mass.Z


class AnomalousGFE(AbstractModel):
    def __init__(self, mu, r, v, a):
        super().__init__()
        self.InitialValues.append(r[0][0])
        self.InitialValues.append(r[1][0])
        self.InitialValues.append(r[2][0])
        self.InitialValues.append(v[0][0])
        self.InitialValues.append(v[1][0])
        self.InitialValues.append(v[2][0])

        self.RightParts.append(lambda t, x: x[3])
        self.RightParts.append(lambda t, x: x[4])
        self.RightParts.append(lambda t, x: x[5])

        self.RightParts.append(lambda t, x: acceleration(mu, x[0], x[1], x[2], a)[0] + dgx(mu, x[0], x[1], x[2]))
        self.RightParts.append(lambda t, x: acceleration(mu, x[0], x[1], x[2], a)[1] + dgy(mu, x[0], x[1], x[2]))
        self.RightParts.append(lambda t, x: acceleration(mu, x[0], x[1], x[2], a)[2] + dgz(mu, x[0], x[1], x[2]))


def r3(x, y, z, i):
    return ((x - X[i])**2 + (y - Y[i])**2 + (z - Z[i])**2)**1.5


def summ(x, y, z, var):
    result = 0
    if var == 'x':
        for i in range(len(MASS)):
            result += (MASS[i] / r3(x, y, z, i)) * (x - X[i])
    if var == 'y':
        for i in range(len(MASS)):
            result += (MASS[i] / r3(x, y, z, i)) * (y - Y[i])
    if var == 'z':
        for i in range(len(MASS)):
            result += (MASS[i] / r3(x, y, z, i)) * (z - Z[i])
    return result


def dgx(mu, x, y, z):
    return -mu * summ(x, y, z, 'x')


def dgy(mu, x, y, z):
    return -mu * summ(x, y, z, 'y')


def dgz(mu, x, y, z):
    return -mu * summ(x, y, z, 'z')
