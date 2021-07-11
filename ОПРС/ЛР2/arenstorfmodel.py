from abstractinterface import AbstractModel
import math


class ArenstorfModel(AbstractModel):
    def __init__(self):
        super().__init__()

        self.InitialValues.append(0.994)  # z1
        self.InitialValues.append(0)  # z2
        self.InitialValues.append(0)  # z3
        self.InitialValues.append(-2.00158510637908252240537862224)  # z4

        C1 = 0.987722529
        C2 = 0.012277471

        # z = [z1, z2, z3, z4]

        self.RightParts.append(lambda t, z: z[2])  # z1'

        self.RightParts.append(lambda t, z: z[3])  # z2'

        self.RightParts.append(
            lambda t, z: z[0] + 2 * z[3] - C1 * (z[0] + C2) / ((z[0] + C2) ** 2 + z[1] ** 2) ** 1.5 - C2 * (
                        z[0] - C1) / ((z[0] - C1) ** 2 + z[1] ** 2) ** 1.5)  # z3'

        self.RightParts.append(
            lambda t, z: z[1] - 2 * z[2] - C1 * z[1] / ((z[0] + C2) ** 2 + z[1] ** 2) ** 1.5 - C2 * z[1] / (
                        (z[0] - C1) ** 2 + z[1] ** 2) ** 1.5)  # z4'


class Test(AbstractModel):
    def __init__(self):
        super().__init__()

        self.InitialValues.append(0)

        self.RightParts.append(lambda x, y: math.exp(-3 * x))
