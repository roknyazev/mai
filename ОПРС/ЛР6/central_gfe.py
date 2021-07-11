from dpintegrator import AbstractModel


class CentralGFE(AbstractModel):
    def __init__(self, mu, r, v):
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

        self.RightParts.append(lambda t, x: -mu * x[0] / (mod(x)) ** 3)
        self.RightParts.append(lambda t, x: -mu * x[1] / (mod(x)) ** 3)
        self.RightParts.append(lambda t, x: -mu * x[2] / (mod(x)) ** 3)


def mod(x):
    return (x[0] ** 2 + x[1] ** 2 + x[2] ** 2) ** 0.5
