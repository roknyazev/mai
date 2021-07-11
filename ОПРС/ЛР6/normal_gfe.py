from dpintegrator import AbstractModel
import numpy as np


class NormalGFE(AbstractModel):
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

        self.RightParts.append(lambda t, x: acceleration(mu, x[0], x[1], x[2], a)[0])
        self.RightParts.append(lambda t, x: acceleration(mu, x[0], x[1], x[2], a)[1])
        self.RightParts.append(lambda t, x: acceleration(mu, x[0], x[1], x[2], a)[2])


def mod(x):
    return (x[0] ** 2 + x[1] ** 2 + x[2] ** 2) ** 0.5


def delta(k):
    if k == 0:
        return 1/2
    else:
        return 1


def p(n, m, phi):
    if n == m and n != 0:
        return p(n-1, m-1, phi) * np.cos(phi) * ((2 * n + 1)/(2 * n * delta(m-1)))**0.5
    elif n > m:
        return p(n-1, m, phi) * np.sin(phi) * ((4 * n**2 - 1)/(n**2 - m**2))**0.5 - p(n-2, m, phi) *\
               ((((n-1)**2 - m**2) * (2 * n + 1))/((n**2 - m**2)*(2 * n - 3)))**0.5
    elif n < m:
        return 0
    elif n == m and m == 0:
        return 1


def p_(n, pn1):
    return (0.5 * n * (n + 1))**0.5 * pn1


def j(n):
    if n == 2:
        return 1082.62575e-6
    if n == 4:
        return -2.37089e-6
    if n == 6:
        return 6.08e-9
    if n == 8:
        return -1.40e-11


def c(n):
    return -(j(n) / (2 * n + 1)**0.5)


def elem1(n, a, ro, phi):
    return (n + 1) * (((a/ro)**n) * c(n) * p(n, 0, phi))


def elem2(n, a, ro, phi):
    pn1 = p(n, 1, phi)
    return ((a/ro)**n) * c(n) * p_(n, pn1)


def acceleration(mu, x, y, z, a):
    X = [x, y, z]
    ro = mod(X)
    r_0 = (x**2 + y**2)**0.5
    phi = np.arctan2(z, r_0)
    sum1 = elem1(2, a, ro, phi) + elem1(4, a, ro, phi) + elem1(6, a, ro, phi) + elem1(8, a, ro, phi)
    sum2 = elem2(2, a, ro, phi) + elem2(4, a, ro, phi) + elem2(6, a, ro, phi) + elem2(8, a, ro, phi)
    gp = -mu/(ro**2) - mu/(ro**2) * sum1
    gf = mu/(ro**2) * sum2
    gl = 0
    vec = np.array([[gp], [gf], [gl]])
    A = np.array([[x/ro, -x*z/(ro * r_0), -y/r_0],
                  [y/ro, -y*z/(ro * r_0), x/r_0],
                  [z/ro, r_0/ro, 0]])
    result = A.dot(vec)
    return [result[0][0], result[1][0], result[2][0]]
