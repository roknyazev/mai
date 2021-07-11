from measurements import measurement_sim
import matplotlib
import matplotlib.pyplot as plt
from kalman_filter import *
import numpy as np

matplotlib.use('Qt5Agg')

ERROR = 2

TIME, MEASUREMENT, TRUE_POPULATION = measurement_sim(ERROR)

CORRECTED_VEC = np.array([1, 1])
CORRECTED_COV = np.array([[0.0001, 0], [0, 0.0001]])

RESULT = [CORRECTED_VEC]
PIPE1 = [[1 + 3 * CORRECTED_COV[1, 1]**0.5, 1 - 3 * CORRECTED_COV[1, 1]**0.5]]
PIPE2 = [[1 + 3 * 0.04, 1 - 3 * 0.04]]
COV = [0.0001]

for i in range(1, len(TIME)):
    dt = TIME[i] - TIME[i - 1]
    CORRECTED_VEC, CORRECTED_COV = kalman(CORRECTED_VEC, CORRECTED_COV, MEASUREMENT[:, i], dt,
                                          rand_err_args=[ERROR, CORRECTED_VEC[1]])
    RESULT.append(CORRECTED_VEC[0])
    COV.append(CORRECTED_COV[0, 0])
    PIPE1.append([TRUE_POPULATION[0][i] + 3 * CORRECTED_COV[1, 1]**0.5, TRUE_POPULATION[0][i] - 3 * CORRECTED_COV[1, 1]**0.5])
    PIPE2.append([TRUE_POPULATION[1][i] + CORRECTED_VEC[0] * 0.07,
                  TRUE_POPULATION[1][i] - CORRECTED_VEC[0] * 0.084])

#plt.plot(TIME, COV)

#plt.plot(TIME, PIPE1)
#plt.plot(TIME, PIPE2)
plt.plot(TIME, TRUE_POPULATION[0])
plt.plot(TIME, TRUE_POPULATION[1])
#plt.plot(TIME, TRUE_POPULATION[1])
plt.plot(TIME[1:-1], RESULT[1:-1])

plt.show()
