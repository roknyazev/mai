from ml_getdata import get_data_from_variable
from random import gauss
import numpy as np
import copy


def measurement_sim(error):
    """
    Симулирует реальный подсчет популяции
    :param error: Среднеквадратическое отклонение гауссовской ошибки (% от популяции)
    :return:
    """
    data = get_data_from_variable('data/predators_population.mat', 'out')
    true_data = copy.copy(data)
    time = data[0]
    pred_population = data[1]
    prey_population = np.zeros_like(pred_population)
    for i in range(len(pred_population)):
        pred_population[i] += gauss(0, error*pred_population[i]*0.01)
        prey_population[i] = None
    res = np.array([prey_population, pred_population])
    return time, res, [true_data[1], true_data[2]]
