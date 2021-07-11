from dpintegrator import AbstractModel


class KeplerEphemerisModel(AbstractModel):
    def __init__(self):
        super().__init__()
        # 01.01.2020 0:00 UTC
        self.JD = 2458849.5
        X = -2.544849737206064e7
        Y = 1.340363435046712e8
        Z = 5.810843791233169e7
        Vx = -2.986035979849415e1
        Vy = -4.729400174042427
        Vz = 2.049672198684736
        mu = 132712.43994e6
        self.InitialValues.append(X)
        self.InitialValues.append(Y)
        self.InitialValues.append(Z)
        self.InitialValues.append(Vx)
        self.InitialValues.append(Vy)
        self.InitialValues.append(Vz)

        self.RightParts.append(lambda t, x: x[3])
        self.RightParts.append(lambda t, x: x[4])
        self.RightParts.append(lambda t, x: x[5])

        self.RightParts.append(lambda t, x: -mu * x[0] / (mod(x)) ** 3)
        self.RightParts.append(lambda t, x: -mu * x[1] / (mod(x)) ** 3)
        self.RightParts.append(lambda t, x: -mu * x[2] / (mod(x)) ** 3)


def mod(x):
    return (x[0]**2 + x[1]**2 + x[2]**2)**0.5
