from abstractinterface import AbstractModel


class IdealMathPendulum(AbstractModel):
    def __init__(self, m, d):
        super().__init__()

        self.m = m
        self.d = d
        self.g = 9.81

        self.InitialValues.append(1)  # z0
        self.InitialValues.append(0)  # z1

        self.RightParts.append(lambda t, z: z[1])  # z1'
        self.RightParts.append(lambda t, z: (- z[0] * self.m * self.g / self.d))


class MathPendulum(AbstractModel):
    def __init__(self, m, d, c):
        super().__init__()

        self.m = m
        self.d = d
        self.c = c
        self.g = 9.81

        self.InitialValues.append(1)  # z0
        self.InitialValues.append(0)  # z1

        self.RightParts.append(lambda t, z: z[1])  # z0'
        self.RightParts.append(lambda t, z: (-self.c * self.g / self.d * z[1] - z[0] * self.m * self.g / self.d))  # z1'


class IdealSpringPendulum(AbstractModel):
    def __init__(self, m, k):
        super().__init__()

        self.m = m
        self.k = k

        self.InitialValues.append(1)  # z0
        self.InitialValues.append(0)  # z1

        self.RightParts.append(lambda t, z: z[1])  # z0'
        self.RightParts.append(lambda t, z: (- z[0] * self.k / self.m))  # z1'


class SpringPendulum(AbstractModel):
    def __init__(self, m, k, ms, mv):
        super().__init__()

        self.m = m
        self.k = k
        self.ms = ms
        self.mv = mv
        self.g = 9.81

        self.InitialValues.append(1)  # z0
        self.InitialValues.append(0)  # z1

        self.RightParts.append(lambda t, z: z[1])

        self.RightParts.append(lambda t, z: (- z[0] * self.k / self.m - self.g * self.ms - self.mv * z[1] / self.m))


